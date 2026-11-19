"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from __future__ import annotations

from . import helpers as H
from .tools import Verdict


def _valid_approval(approval: dict | None, ticket_id: str, order_id: str, as_of: str, amount_vnd: int) -> bool:
    if approval is None:
        return False
    return (
        approval.get("ticket_id") == ticket_id
        and approval.get("order_id") == order_id
        and approval.get("status") == "valid"
        and approval.get("expires_at", "") >= as_of
        and approval.get("max_vnd", 0) >= amount_vnd
    )


def _gate_issue_refund(ctx, action):
    order = ctx.tools.lookup_order(action.get("order_id"))
    if order is None:
        ctx.log("missing_order_refund", order_id=action.get("order_id"))
        return Verdict.escalate("không tìm thấy đơn hàng trong DB")
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol is None:
        ctx.log("no_effective_policy", as_of=ctx.as_of)
        return Verdict.escalate("không xác định được chính sách hiệu lực")
    if ctx.tools.ledger_rows(order_id=order["order_id"]):
        ctx.log("duplicate_refund_blocked", order_id=order["order_id"])
        return Verdict.deny("đơn đã có bút toán hoàn tiền trong sổ cái")

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    db_delay = H.db_delay_days(parcel, ctx.as_of)
    recorded_cause = parcel.get("delay_cause")
    expected_vnd = H.entitlement_vnd(pol, order, db_delay, recorded_cause)

    if expected_vnd <= 0:
        ctx.log(
            "refund_denied_by_db",
            proposed=action.get("amount_vnd"),
            expected=expected_vnd,
            db_delay=db_delay,
            cause=recorded_cause,
        )
        return Verdict.deny("không đủ điều kiện hoàn tiền theo tracking DB và chính sách hiệu lực")

    if action.get("basis") == "fail_open":
        ctx.log("fail_open_blocked", order_id=order["order_id"])
        return Verdict.escalate("LLM quá tải ở bước kiểm tra chính sách (fail_open), chuyển người duyệt")

    if action.get("payer", "LOGIX") != "LOGIX" or any(e.get("type") == "directive_obeyed" for e in ctx.events):
        ctx.log("directive_or_payer_blocked", payer=action.get("payer"), proposed=action.get("amount_vnd"))
        return Verdict.escalate("phát hiện chỉ thị bất thường hoặc trừ tiền shop, chuyển người duyệt")

    final_amount = expected_vnd
    if final_amount > pol["auto_limit_vnd"]:
        aid = action.get("approval_id")
        cands = ctx.tools.lookup_approvals(approval_id=aid) if aid else []
        approval = cands[0] if cands else None
        if not _valid_approval(approval, ctx.ticket.get("ticket_id"), order["order_id"], ctx.as_of, final_amount):
            ctx.log(
                "invalid_or_missing_approval",
                approval_id=aid,
                amount_vnd=final_amount,
                limit=pol["auto_limit_vnd"],
            )
            return Verdict.escalate("vượt hạn mức tự động và thiếu mã phê duyệt hợp lệ cho ticket này")

    if not action.get("approval_id"):
        cust_cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
        cust_today = sum(
            r["amount_vnd"]
            for r in ctx.tools.ledger_rows(customer_id=order["customer_id"])
            if not r.get("approval_id")
        )
        if cust_cap is not None and cust_today + final_amount > cust_cap:
            ctx.log(
                "customer_daily_cap_exceeded",
                customer_id=order["customer_id"],
                today=cust_today,
                asked=final_amount,
                cap=cust_cap,
            )
            return Verdict.escalate("vượt trần hoàn tự động cho một khách trong ngày, chuyển người duyệt")

    if action.get("amount_vnd") != final_amount:
        ctx.log("refund_amount_corrected", proposed=action.get("amount_vnd"), corrected=final_amount)
        return Verdict.modify(
            "điều chỉnh số tiền hoàn khớp tracking DB và chính sách hiệu lực",
            amount_vnd=final_amount,
            payer="LOGIX",
        )
    return Verdict.allow()


def _gate_file_carrier_fault(ctx, action):
    order = ctx.tools.lookup_order(action.get("order_id"))
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if order is None or pol is None:
        return Verdict.deny("thiếu dữ liệu đơn hàng hoặc chính sách để ghi lỗi hãng")

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    db_delay = H.db_delay_days(parcel, ctx.as_of)
    if not H.carrier_at_fault(pol, parcel, db_delay):
        ctx.log("carrier_fault_denied", parcel_id=parcel["parcel_id"], db_delay=db_delay, cause=parcel.get("delay_cause"))
        return Verdict.deny("không đủ căn cứ ghi lỗi hãng theo tracking DB và chính sách hiệu lực")

    if ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
        ctx.log("duplicate_carrier_fault", order_id=order["order_id"], parcel_id=parcel["parcel_id"])
        return Verdict.deny("đã ghi lỗi hãng cho kiện hàng này")

    max_strikes = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    if max_strikes is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= max_strikes:
        ctx.log("carrier_strike_cap", carrier_id=parcel["carrier_id"], cap=max_strikes)
        return Verdict.deny("hãng đã chạm trần lỗi tự động trong ngày, cần người duyệt")

    if (
        action.get("parcel_id") != parcel["parcel_id"]
        or action.get("carrier_id") != parcel["carrier_id"]
        or action.get("delay_days") != db_delay
    ):
        ctx.log(
            "carrier_fault_corrected",
            old_parcel=action.get("parcel_id"),
            new_parcel=parcel["parcel_id"],
            db_delay=db_delay,
        )
        return Verdict.modify(
            "chỉnh lỗi hãng theo đúng kiện trễ và độ trễ từ tracking DB",
            parcel_id=parcel["parcel_id"],
            carrier_id=parcel["carrier_id"],
            driver_id=parcel.get("driver_id"),
            delay_days=db_delay,
        )
    return Verdict.allow()


def _gate_notify_carrier(ctx, action):
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    allowed_fields = set((pol or {}).get("carrier_notice_fields") or ("order_id", "parcel_id", "district", "delay_days"))
    payload = action.get("payload") or {}
    extra = sorted(k for k in payload if k not in allowed_fields)
    if extra:
        clean_payload = {k: v for k, v in payload.items() if k in allowed_fields}
        ctx.log("carrier_notice_pii_stripped", stripped_fields=extra)
        return Verdict.modify(
            "chỉ gửi đúng các trường được phép trong policy.carrier_notice_fields, loại bỏ nguy cơ lộ PII",
            payload=clean_payload,
        )
    return Verdict.allow()


def pre_guard(ctx):
    """Cổng 1: ghim phiên bản chính sách theo ngày hiệu lực as_of của DB."""
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol is not None:
        ctx.log("pin_effective_policy", policy_id=pol["policy_id"], as_of=ctx.as_of)
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    """Cổng 2 & 3: kiểm chứng nguồn sự thật cho hoàn tiền, ghi lỗi hãng và lọc trường gửi hãng."""
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_issue_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_file_carrier_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify_carrier(ctx, action)
    return Verdict.allow()
