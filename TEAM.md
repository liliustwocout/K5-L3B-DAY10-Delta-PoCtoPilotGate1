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

*(Điền trong và cuối buổi lab; ghi rõ nếu có dùng trợ lý AI cho phần việc nào.)*

### Bằng chứng

*(Mã commit, mã lần chạy `runs/<mã>`, dòng trong phiếu.)*

### Exit ticket

*(Một điều học được, một điều còn chưa chắc.)*

## TranDucDuy-2A202604071

### Phần việc phụ trách

Vai trong bàn: **Kỹ sư cổng**.
Phụ trách: cùng phụ trách phần kỹ thuật cổng phòng ngừa và kiểm thử — câu 1.3 (Phiếu A mục A2 cột Offline), câu 1.5 (cùng bàn, A3); câu 2.1–2.2 (Phiếu B mục B0–B2), câu 2.5 (cùng bàn, B6), câu 2.6–2.8 (Phiếu B mục B7.1–B7.3, viết behavioral test và ticket hiểm `--adhoc`); vòng 2 dò trace sự cố, sửa `pre_guard`/`write_gate`, bổ sung và kiểm tra monitor mới cho câu 3.0–3.1, 3.4–3.6 (Phiếu C mục C0–C2, C6–C8). File chính: `lab10/guards.py`, `lab10/monitors.py`.

### Đóng góp cụ thể

*(Điền trong và cuối buổi lab; ghi rõ nếu có dùng trợ lý AI cho phần việc nào.)*

### Bằng chứng

*(Mã commit, mã lần chạy `runs/<mã>`, dòng trong phiếu.)*

### Exit ticket

*(Một điều học được, một điều còn chưa chắc.)*

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

*(Điền trong và cuối buổi lab; ghi rõ nếu có dùng trợ lý AI cho phần việc nào.)*

### Bằng chứng

*(Mã commit, mã lần chạy `runs/<mã>`, dòng trong phiếu.)*

### Exit ticket

*(Một điều học được, một điều còn chưa chắc.)*
