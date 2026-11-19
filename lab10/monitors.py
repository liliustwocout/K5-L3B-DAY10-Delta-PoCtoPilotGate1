"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def fail_open_rate(trials):
    """Tỷ lệ trial xảy ra fallback fail_open khi LLM quá tải ở bước kiểm tra chính sách."""
    if not trials:
        return 0.0
    hits = sum(
        any(e.get("type") == "llm_fallback" and e.get("mode") == "fail_open" for e in (t.get("events") or []))
        for t in trials
    )
    return hits / len(trials)


def max_queue_wait_min(trials):
    """Thời gian chờ người duyệt lâu nhất (phút) trong các ca vào hàng chờ."""
    waits = [t["queue_wait_min"] for t in trials if t.get("queue_wait_min") is not None]
    return float(max(waits)) if waits else 0.0


def max_daily_auto_refund_vnd(trials):
    """Tổng tiền hoàn tự động (không có approval_id) cao nhất trong một ngày giả lập."""
    by_day = {}
    for t in trials:
        key = (t.get("seed"), t.get("day"))
        auto = sum(r.get("amount_vnd", 0) for r in (t.get("ledger") or []) if not r.get("approval_id"))
        by_day[key] = by_day.get(key, 0) + auto
    return float(max(by_day.values())) if by_day else 0.0


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "fail_open_rate": fail_open_rate,
    "max_queue_wait_min": max_queue_wait_min,
    "max_daily_auto_refund_vnd": max_daily_auto_refund_vnd,
}
STARTER_MONITORS = ("escalation_rate",)
