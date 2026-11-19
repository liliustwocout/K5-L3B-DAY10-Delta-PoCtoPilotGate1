# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Delta`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Delta-PoCtoPilotGate1`
- Bản Lab 9 chung của bàn: `docs/lab9/eval_card.md` và `docs/lab9/PRD_v1.1.md` (nguồn: bài Lab 9 của Lê Phạm Thành Đạt - `2A202604027`)
- Thẻ sự cố đã bốc (S1–S8):

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

*(Điền trong và cuối buổi lab; ghi rõ nếu có dùng trợ lý AI cho phần việc nào.)*

### Bằng chứng

*(Mã commit, mã lần chạy `runs/<mã>`, dòng trong phiếu.)*

### Exit ticket

*(Một điều học được, một điều còn chưa chắc.)*

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
