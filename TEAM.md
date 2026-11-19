# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Delta`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Delta-PoCtoPilotGate1`
- Bản Lab 9 chung của bàn: `docs/lab9/eval_card.md` và `docs/lab9/PRD_v1.1.md` (nguồn: bài Lab 9 của Lê Phạm Thành Đạt - `2A202604027`)
- Thẻ sự cố đã bốc (S1–S8): `S4`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Lê Phạm Thành Đạt | 2A202604027 | Kỹ sư cổng | x |
|   2 | Trần Đức Duy | 2A202604071 | Kỹ sư cổng | |
|   3 | Phạm Hoàng Đức Minh | 2A202604114 | Sản phẩm và kinh doanh | |
|   4 | Nguyễn Ngọc Bách | 2A202604108 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## LePhamThanhDat-2A202604027

### Phần việc phụ trách

Vai trong bàn: **Kỹ sư cổng (Trưởng nhóm)**.
Phụ trách: thiết lập repo nhóm & cấu hình ban đầu; câu 1.3 (Phiếu A mục A2 cột Offline), cùng bàn làm câu 1.5 (A3); câu 2.1–2.2 (Phiếu B mục B0, B1, B2), câu 2.5 (cùng bàn, B6), câu 2.6–2.8 (Phiếu B mục B7.1–B7.3); vòng 2 chạy `lab10.grade`, dò trace sự cố, sửa cổng kỹ thuật và thêm monitor mới cho câu 3.0–3.1, 3.4–3.6 (Phiếu C mục C0–C2, C6–C8). File chính: `lab10/guards.py`, `lab10/monitors.py`, `TEAM.md`.

### Đóng góp cụ thể

- Khởi tạo và thiết lập repo nhóm (CP1), chọn bộ tài liệu Lab 9 chung (`docs/lab9/eval_card.md`, `docs/lab9/PRD_v1.1.md`), cấu hình danh tính Git và chuẩn hóa line ending LF (`.gitattributes`) cho cả nhóm trên Windows.
- Hoàn thiện phần Kỹ sư cổng ở Phiếu A: câu 1.3 (cột Offline bước `file_carrier_fault`) và bảng ghi nhận ký tiêu chí A5.
- Vòng 1 (CP3): chạy đánh giá mốc `base`, dò trace `T-002@55`, thiết kế behavioral test `--adhoc` (O-1002, O-1004); code 3 cổng phòng ngừa vòng 1 trong `lab10/guards.py` (`pre_guard` ghim `policy_id` theo `as_of`, `write_gate` cho `issue_refund`, `file_carrier_fault`, `notify_carrier`); điền Phiếu B (B0, B1, B2, B6 3 dòng Kỹ thuật, B7.1–B7.3) và hoàn thiện chốt cổng vòng 1 (`lab10.checkpoint`, hash `7e724506`).
- Vòng 2 (CP4–CP5): kéo gói thẻ `S4` (`incidents/S4/`), ghi nhận thẻ vào các file nộp bài, hoàn thiện Phiếu C (mục C1, C6, C9 và rà soát đồng bộ số liệu C0, C7, C12 với `operating_gates.json`), chạy kiểm tra cuối (`lab10.grade --incident S4`) và gom bài nộp (`lab10.check_submission --collect`).
- *(Có sử dụng trợ lý AI hỗ trợ đọc trace, rà soát tính nhất quán dữ liệu/hash/line-ending và hoàn thiện trình bày trong các phiếu.)*

### Bằng chứng

- Các commit: `e4655c4` (CP1), `e976745` (CP2 Phiếu A), `e53a8c4` (CP3 cổng vòng 1 & Phiếu B), `c514462` (chốt `operating_gates.round1.json` & `round1.lock`), `4b78187` (Nhận thẻ `S4`), `d70fa46` (ghi nhận `S4` vào Form C/TEAM/submission).
- Code & file chốt: `lab10/guards.py`, `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`.
- Mã lần chạy: `R-base-before-20261119-155033-64a6fd`, `R-base-after-20261119-155643-654054`, `R-base-after-20261119-174404-c66ec6`, `R-S4-grade-20261119-165644-46871d`, `R-S4-grade-20261119-174404-c66ec6` (`PASS-VISIBLE`).
- Các mục trong phiếu: Phiếu A (A2 câu 1.3, A5), Phiếu B (B0–B2, B6, B7.1–B7.3), Phiếu C (C0, C1, C6, C9, C12).

### Exit ticket

- **Một điều học được:** Các cổng phòng ngừa cấp hệ thống nằm ngoài LLM (đối chiếu nguồn sự thật tracking DB, ghim phiên bản chính sách và chặn ngưỡng chi tiêu) mới là lớp bảo vệ quyết định giúp ngăn lỗi chìm ngay cả khi model gặp lỗi 429 hoặc bị dữ liệu khách khai đánh lừa.
- **Một điều còn chưa chắc:** Khi triển khai thực tế mà lưu lượng ở riêng 2 kho HN và HCM cùng tăng gấp đôi so với bộ S4, cơ chế gọi thêm reviewer dự phòng ngoài đời thực cần thời gian kích hoạt tối đa bao nhiêu phút để giữ được SLA 60 phút.

## TranDucDuy-2A202604071

### Phần việc phụ trách

Vai trong bàn: **Kỹ sư cổng**.
Phụ trách: cùng phụ trách phần kỹ thuật cổng phòng ngừa và kiểm thử — câu 1.3 (Phiếu A mục A2 cột Offline), câu 1.5 (cùng bàn, A3); câu 2.1–2.2 (Phiếu B mục B0–B2), câu 2.5 (cùng bàn, B6), câu 2.6–2.8 (Phiếu B mục B7.1–B7.3, viết behavioral test và ticket hiểm `--adhoc`); vòng 2 dò trace sự cố, sửa `pre_guard`/`write_gate`, bổ sung và kiểm tra monitor mới cho câu 3.0–3.1, 3.4–3.6 (Phiếu C mục C0–C2, C6–C8). File chính: `lab10/guards.py`, `lab10/monitors.py`.

### Đóng góp cụ thể

- Tham gia rà soát thiết kế cổng phòng ngừa vòng 1 và kiểm thử luồng xử lý cùng nhóm Kỹ sư cổng.
- Vòng 2 (thẻ `S4`): trực tiếp dò trace các ca hỏng theo nhiều kiểu khác nhau (`S4-08@11`, `S4-05@11`, `S4-07@11`), phân tích nguyên nhân LLM 429 dẫn tới `fail_open` và lỗ hổng config ngày sale chưa đồng bộ `ops_limits.daily_auto_refund_budget_vnd` (`300.000đ`).
- Gia cố `lab10/guards.py` (nhánh `_gate_issue_refund`) bổ sung cơ chế chặn trần hoàn tự động động theo `min(ops_limits.daily_auto_refund_budget_vnd, business.daily_refund_cap_vnd)` (ghi sự kiện `daily_refund_budget_exceeded`).
- Thiết kế và cài đặt 3 hàm chỉ số theo dõi mới trong `lab10/monitors.py` (`fail_open_rate`, `max_queue_wait_min`, `max_daily_auto_refund_vnd`), bảo đảm cả 3 monitor đều "sáng đèn" giữa bộ nền và gói sự cố `S4`.
- Điền đầy đủ mục C0 (nhật ký các lần chạy vòng 2), C2 (bảng soát lỗi thẻ S4), và C8 (đặc tả 3 chỉ số theo dõi mới) trong Phiếu C (`templates/form-c-incident.md`).
- *(Có sử dụng trợ lý AI hỗ trợ rà cấu trúc trường `trial` của `monitors.py` và hoàn thiện bảng soát lỗi C2, bảng đặc tả C8.)*

### Bằng chứng

- Commit: `d77fccc` (`CP4: Enforce dynamic daily refund cap, add S4 monitors, and fill Form C (C0, C2, C8)`).
- Code: `lab10/guards.py` (nhánh `daily_refund_budget_exceeded`), `lab10/monitors.py` (`MONITORS` với 3 hàm mới).
- Mã lần chạy: `R-S4-prepared-20261119-170250-33ea9f`, `R-S4-after-20261119-170822-86b365`, `R-S4-after-20261119-170925-0ec110`, `R-base-after-20261119-170925-0ec110`.
- Phiếu C: mục C0, C2, C8 (`templates/form-c-incident.md`).

### Exit ticket

- **Một điều học được:** Chỉ số theo dõi trên production (`monitors.py`) dù không có nhãn đúng/sai vẫn phát hiện chính xác sự cố (như `fail_open_rate` tăng từ `0.0` lên `0.243`, `max_queue_wait_min` lên `78.0` phút) miễn là gắn log đúng điểm chuyển trạng thái rủi ro.
- **Một điều còn chưa chắc:** Trên mô hình LLM thực tế (không dùng MockLLM), cần hiệu chỉnh ngưỡng báo động vàng/đỏ của `fail_open_rate` theo cửa sổ thời gian bao lâu để phát hiện nghẽn API mà không gây cảnh báo giả trong các đợt biến động nhỏ.

## PhamHoangDucMinh-2A202604114

### Phần việc phụ trách

Vai trong bàn: **Sản phẩm và kinh doanh**.
Phụ trách: câu 1.1 (Phiếu A mục A1), câu 1.5 (cùng bàn, A3), câu 1.6 (Phiếu A mục A4–A5: viết Bản tiêu chí, ranh giới đầu ra, điền & ký `config/acceptance_criteria.json`); câu 2.3 (Phiếu B mục B3: bản đồ dữ liệu và ví dụ drift), câu 2.5 (cùng bàn, lăng kính kinh doanh trong B6), câu 2.9 (Phiếu B mục B7.4: cổng `business`), chủ trì quyết định v1 (Phiếu B mục B8); vòng 2 viết specification câu 3.2 (Phiếu C mục C5), cùng bàn làm fault tree (C6), chỉnh cổng `business` ở câu 3.5 (C7), đọc chi phí/ROI/trần tiền và viết quyết định v2 (Phiếu C mục C12). File chính: `config/acceptance_criteria.json`, `config/operating_gates.json` (mục `business`), Phiếu A, Phiếu B (B3, B6, B7.4, B8), Phiếu C (C5, C12).

### Đóng góp cụ thể

- Chủ trì thiết lập Bản tiêu chí chấp nhận trong `config/acceptance_criteria.json` với các ranh giới đỏ nghiêm ngặt: hoàn sai = 0đ, lỗi hãng oan = 0 ca, rò rỉ PII = 0 ca; các chỉ số kinh doanh & vận hành: trần chi phí mỗi ticket ≤ 8.000đ (tiết kiệm ít nhất 20% so với làm tay 10.000đ theo `ops_facts`), ROI tối thiểu 20%, không để ticket bị ùn quá 60 phút.
- Trực tiếp ký số niêm phong tiêu chí (`lab10.criteria sign`, commit `4f7f982`) trước khi chạy bất kỳ đánh giá nào.
- Thiết lập cổng an toàn kinh doanh trong `config/operating_gates.json` (mục `business`): trần ngân sách hoàn tự động 2.000.000đ/ngày (`ops_limits.daily_auto_refund_budget_vnd`), trần chi phí LLM 1.500đ/ticket (`ops_limits.max_llm_cost_per_ticket_vnd`), phạm vi pilot giới hạn ở 2 kho bán lẻ HN và HCM (chủ động loại trừ kho HCM-B2B có đơn sỉ ≥ 2 triệu đồng để phòng ngừa rủi ro tài chính).
- Phân tích luồng dữ liệu nghiệp vụ và cảnh báo rủi ro Concept Drift / Policy Drift v4 (áp dụng từ 01/12/2026 trong `data/world.json`) đối với các ca trễ do thiên tai bão lũ (`FORCE_MAJEURE`) cấm ghi lỗi hãng vận chuyển.
- Chủ trì đánh giá chỉ số tài chính, ROI và kiểm tra các dòng vượt trần để đưa ra quyết định Gate 1 v1 (mốc `prepared`) và quyết định v2 (sau sự cố S4).
- Viết Specification nghiệp vụ câu 3.2 và đề xuất điều chỉnh cổng ngân sách ngày sale bùng nổ (S4) ở mức 300.000đ để bảo vệ dòng tiền.
- *(Có sử dụng trợ lý AI hỗ trợ rà soát tính nhất quán số liệu từ `data/world.json` và cấu trúc các phiếu A, B, C).*

### Bằng chứng

- File cam kết tiêu chí đã ký: `config/acceptance_criteria.json` và `config/acceptance_criteria.lock` (commit ký `4f7f982`).
- Cấu hình cổng kinh doanh: `config/operating_gates.json` (khối `business`, checkpoint hash `7e724506`).
- Các mục tự viết trong phiếu: Phiếu A (A1 câu 1.1, A3 câu 1.5, A4 câu 1.6, A5 ký tiêu chí); Phiếu B (B3 câu 2.3, B6 lăng kính kinh doanh câu 2.5, B7.4 câu 2.9, B8 quyết định v1); Phiếu C (C5 câu 3.2, C7 câu 3.5, C12 quyết định v2).
- Mã lần chạy thực tế:
  - Mốc base: `R-base-before-20261119-155033-64a6fd` (chi phí 4.203đ, hoàn sai 20.000đ, lỗi hãng oan 1).
  - Mốc prepared: `R-base-prepared-20261119-164658-46871d` (pass rate 1.0, hoàn sai 0đ, lỗi oan 0, chi phí 5.550đ, ROI 0.8).
  - Mốc sự cố S4: chi phí/ticket 6.966đ, ROI 0.44 (44%), độ phủ 0.561, escalation_rate 0.4957, ngân sách ngày sale 300.000đ.

### Exit ticket

- **Một điều học được:** Một hệ thống AI khi chuyển từ PoC sang Pilot không chỉ cần đo độ chính xác mô hình (pass rate) mà quan trọng hơn là phải có các cổng an toàn chặn ranh giới đỏ (ngân sách tài chính, rủi ro đối tác, rò rỉ dữ liệu) để bảo vệ dòng tiền và uy tín doanh nghiệp.
- **Một điều còn chưa chắc:** Cách tối ưu hóa cân bằng giữa tỷ lệ chuyển người duyệt (escalation rate) và thời gian phản hồi của kiểm soát viên CSKH trong các đợt flash-sale cao điểm khi lượng đơn tăng vọt gấp 3-5 lần bình thường.

## NguyenNgocBach-2A202604108

### Phần việc phụ trách

Vai trong bàn: **Vận hành và pháp lý**.
Phụ trách: câu 1.2 (Phiếu A mục A1: góc nhìn kế toán và trưởng ca CSKH), câu 1.4 (Phiếu A mục A2 cột Telemetry production), câu 1.5 (cùng bàn, A3); câu 2.4 (Phiếu B mục B4 HAZOP vòng 1 và B5 checklist 9 nhóm có PIC), câu 2.5 (cùng bàn, lăng kính vận hành & pháp lý trong B6), câu 2.10 (Phiếu B mục B7.5–B7.6: cổng `operations` & `legal`, runbook phần 1–3 và Giờ cao điểm); vòng 2 phụ trách phần riêng của thẻ và HAZOP của thẻ (câu 3.1, Phiếu C mục C3–C4), giả định môi trường (câu 3.3, Phiếu C mục C5), cùng bàn làm fault tree (C6), chỉnh cổng `operations` & `legal` (câu 3.5, C7), cập nhật fault tree sau sửa, risk register, checklist và runbook phần 4–5 (câu 3.7, Phiếu C mục C9–C11), hoàn thiện `submission/submission.json` và gom bài nộp. File chính: `config/operating_gates.json` (mục `operations`, `legal`), `submission/submission.json`, Phiếu A (A1 câu 1.2, A2 câu 1.4), Phiếu B (B4–B5, B7.5–B7.6), Phiếu C (C3–C5, C9–C11).

### Đóng góp cụ thể

- Phiếu A (CP2): viết mục tiêu nhìn từ kế toán đối soát (`NV-OANH`) và trưởng ca CSKH (`NV-HANH`) ở câu 1.2; thiết kế Telemetry production ở câu 1.4 và đối chiếu đồng bộ danh sách 5 hãng vận chuyển thật của hệ thống (`GHSH, VNX, LGX, MKD, DNB`).
- Vòng 1 (CP3): điền toàn bộ cổng `operations` (PIC `NV-TUNG`, người duyệt `NV-HANH`, 1 người trực/ca, 6 ca/giờ, SLA 60 phút, bật `decision_note: true`, kiểm mẫu `10%`, kênh `#alerts-logix-ops`, 3 điều kiện dừng) và `legal` (`carrier_fault_requires_recorded_cause: true`, danh sách chặn PII gửi bên thứ ba) trong `config/operating_gates.json`; hoàn thiện HAZOP vòng 1 (B4), checklist 9 nhóm có PIC (B5), Runbook phần 1–3 (B7.5) và Giờ cao điểm (B7.6) trong Phiếu B.
- Vòng 2 (CP4 · thẻ `S4`): bổ sung trường `"recipient_contact"` vào `legal.pii_fields_blocked_to_third_party` trong `config/operating_gates.json`; cập nhật Ghi chú Vòng 2 cho mục Giờ cao điểm B7.6 (phần riêng của thẻ `S4`); soạn HAZOP riêng của thẻ `S4` (C4), giả định môi trường câu 3.3 (C5), 2 dòng Risk register (C10), cập nhật checklist 9 nhóm có PIC và viết Runbook phần 4–5 (C11) trong Phiếu C.
- *(Có sử dụng trợ lý AI hỗ trợ rà soát cấu trúc bảng HAZOP, Runbook vận hành và đối chiếu yêu cầu bảo vệ dữ liệu cá nhân PII.)*

### Bằng chứng

- Các commit: `d2623e8` (`add Operations & Legal role work`), `3bc04c3`, `6be7273` (`fix conflict form a`), `d163d4a` (`report s4 (Vận hành & pháp lý)`).
- Cấu hình: `config/operating_gates.json` (mục `operations` và `legal`).
- Các mục trong phiếu: Phiếu A (A1 câu 1.2, A2 câu 1.4), Phiếu B (B4, B5, B7.5, B7.6 cả hai vòng), Phiếu C (C4, C5 câu 3.3, C10, C11).

### Exit ticket

- **Một điều học được:** Độ tin cậy khi đưa trợ lý AI ra pilot không chỉ nằm ở code chặn lỗi model, mà còn phụ thuộc chặt chẽ vào cổng vận hành và con người (`pilot_scope`, `decision_note`, tỉ lệ kiểm mẫu `10%`, năng lực trực `6 ca/giờ`, và runbook dừng khẩn cấp dưới 5 phút).
- **Một điều còn chưa chắc:** Với tỉ lệ chuyển người duyệt gần `50%` trong ngày flash-sale, quy trình kích hoạt nhân sự dự phòng và đối soát hủy lỗi phạt với hãng vận chuyển (`NV-OANH`) ngoài thực tế cần tự động hóa đến mức nào để luôn kịp cam kết SLA.
