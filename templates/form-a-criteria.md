# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-Delta-PoCtoPilotGate1 (Nhóm Delta · L3B) · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Giảm thời gian xử lý khiếu nại hoàn tiền giao trễ từ 24h xuống dưới 5 phút, tiết kiệm ít nhất 30% chi phí vận hành xử lý sự vụ so với quy trình thủ công (10.000đ/ticket), đồng thời bảo vệ dòng tiền LogiX không để xảy ra hoàn sai hoặc phạt oan đối tác vận chuyển.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Không có chênh lệch giữa tiền hoàn tự động trên sổ cái LogiX với số liệu đối soát của Shop/Hãng; đặc biệt số lỗi ghi phạt hãng vận chuyển (`file_carrier_fault`) phát sinh từ AI phải có căn cứ rõ ràng từ hệ thống tracking để tỷ lệ khiếu nại/phản đối từ các hãng vận chuyển bằng 0 (tránh tranh chấp và giữ vững uy tín đối tác).
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Số lượng ca bị chuyển sang người duyệt (escalation) không được vượt quá năng lực trực ca (tối đa 6 ca/giờ/người, thời gian chờ của khách < 60 phút theo SLA); các quyết định trợ lý chuyển sang phải có ghi chú tóm tắt lý do rõ ràng (`decision_note`), không đẩy các ca rác hoặc lỗi ngớ ngẩn làm quá tải và gây ức chế cho đội ngũ CSKH.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước **ghi lỗi hãng vận chuyển** (`file_carrier_fault`) sau bước tính quyền lợi hoàn tiền (khác ví dụ mẫu "chọn độ trễ"). | Hành vi ghi lỗi/phạt hãng vận chuyển (`file_carrier_fault`) hoặc hoàn tiền tự động (`issue_refund`) gây tác động đối ngoại |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ (%) lệnh `file_carrier_fault` hợp lệ — tức kiện hàng được ghi lỗi đúng là kiện gây trễ thực sự theo tracking DB, có nguyên nhân trễ được ghi nhận thuộc `policy.fault_causes` và độ trễ DB đạt ngưỡng hoàn phí của chính sách hiện hành. | Tỷ lệ khiếu nại phát sinh từ đối tác/hãng vận chuyển trên tổng số ca AI ghi phạt lỗi hãng (đơn vị: %) HOẶC Số lượng yêu cầu tra soát/khiếu nại từ bên ngoài gửi về trong ngày (đơn vị: vụ/ngày) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện `{"type": "tool", "tool": "file_carrier_fault"}` (các trường `order_id`, `parcel_id`, `carrier_id`, `delay_days`) trong `runs/<mã lần chạy>/traces/<ticket>@<seed>.json` (bộ nền 22 ticket × 5 seed = 110 trial; mở rộng cho gói sự cố), đối chiếu nguồn sự thật `data/world.json` (`orders[].parcels`, `policies`, `as_of`). Nhãn chuẩn được tính tự động, tất định bằng code theo `lab10.helpers.ticket_parcel` và `lab10.helpers.carrier_at_fault(effective_policy, parcel, db_delay_days)` (không gán nhãn thủ công). | Hệ thống tiếp nhận khiếu nại đối soát của chị Oanh (`NV-OANH`), đối soát hóa đơn phạt tuần của hãng vận chuyển (VNX, GHTK, GHN); không cần nhãn AI mà lấy trực tiếp từ sự kiện ticket khiếu nại của đối tác |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `N_hợp_lệ / N_tổng × 100%`, trong đó `N_tổng` là tổng số sự kiện `tool == "file_carrier_fault"` trên toàn bộ trial; một sự kiện tính vào `N_hợp_lệ` khi thỏa đồng thời 4 điều kiện: (1) `parcel_id` và `carrier_id` khớp kiện trễ nhất theo `ticket_parcel(order, ticket, as_of)`, (2) `db_delay_days(parcel, as_of) >= effective_policy.late.min_days_fee`, (3) `parcel.delay_cause` khác `null` và thuộc `effective_policy.fault_causes`, (4) không ghi trùng lặp >1 lần cho cùng `(order_id, parcel_id)`. Xử lý ca thiếu/biên: trial không gọi `file_carrier_fault` loại khỏi mẫu số và đếm riêng (`N_không_ghi_lỗi`); nếu `N_tổng = 0` ghi `N/A` (không gán 100%); nếu thiếu `order_id`/`parcel_id` trong DB tính là không hợp lệ (`0`). | Tổng số vụ hãng/shop gửi văn bản khiếu nại phạt oan chia cho tổng số lệnh `file_carrier_fault` do AI tự động ghi trong kỳ đối soát. Nếu kỳ đó AI không ghi lỗi hãng nào thì mẫu số = 0, ghi nhận vi phạm = 0 |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo dõi hàng ngày (rolling 24h) và tổng kết kỳ đối soát hàng tuần (7 ngày). Ngưỡng báo động: >= 1 vụ khiếu nại ghi phạt oan từ hãng trong tuần HOẶC tổng tiền khiếu nại lệch > 0đ |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | (1) Không đo lỗi bỏ sót (*false negative*) khi hãng thực sự gây trễ nhưng agent không gọi `file_carrier_fault`; (2) không phát hiện được khi chính tracking DB ghi sai `delivered_date` hoặc `delay_cause`; (3) không bắt được lỗi vượt trần vận hành `max_auto_strikes_per_carrier_per_day` (≥ 3 lỗi/hãng/ngày) hay rò rỉ PII ở bước `notify_carrier` phía sau. | Không phát hiện được trường hợp hãng vận chuyển bị phạt oan nhưng chấp nhận bỏ qua không khiếu nại vì số tiền phạt quá nhỏ, hoặc khiếu nại bị gửi trễ sau chu kỳ đối soát (sau 1-2 tuần) |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Chưa đủ căn cứ thống kê để khẳng định Y tốt hơn X vì khoảng tin cậy 95% của X ([0.94, 1.0]) bao trùm cả kết quả của Y (1.0); sự chênh lệch 1 lần chạy (49/50 so với 50/50) hoàn toàn có thể chỉ do biến thiên ngẫu nhiên của mẫu thử.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass rate của trợ lý hoàn tiền trên bộ thử nền (base) hoặc bộ sự cố tụt dưới 0.95 thì chúng tôi sẽ Cải tiến thêm trong 24 giờ trước khi cho phép triển khai pilot. | Nếu pass rate tụt dưới 0.90 thì chúng tôi sẽ Dừng triển khai để đánh giá lại toàn diện pipeline mô hình. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ pass^k (đúng cả 5/5 seed) trên bộ thử tụt dưới 0.90 thì chúng tôi sẽ Thu hẹp phạm vi pilot về 1 kho ổn định nhất (HN) để kiểm soát độ biến thiên. | |
| `wrongful_refund_vnd_max` | Nếu tổng số tiền hoàn sai của trợ lý hoàn tiền trên bất kỳ bộ thử nào vượt quá 0 VND thì chúng tôi sẽ lập tức Dừng tự động hoàn tiền và chuyển toàn bộ sang xử lý thủ công. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0 thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp. | |
| `pii_leaks_max` | Nếu phát hiện số ca rò rỉ dữ liệu cá nhân (PII) khách hàng ra đối tác vượt quá 0 ca thì chúng tôi sẽ Dừng toàn bộ hệ thống ngay lập tức để rà soát an ninh và pháp lý. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt trên bộ thử vượt quá 0.25 (25%) thì chúng tôi sẽ Thu hẹp quy mô pilot hoặc bổ sung thêm nhân sự trực ca để bảo đảm SLA dưới 60 phút. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Không bao giờ tự động hoàn tiền vượt quá 200.000đ cho một ticket và không hoàn vượt ngân sách ngày 2.000.000đ.
- Ngưỡng chuyển cho người duyệt: Mọi đơn trễ có nguyên nhân bất khả kháng hoặc số tiền khiếu nại > 200.000đ hoặc khách tự khai lệch với tracking đều phải chuyển cho nhân viên duyệt (chị Hạnh).

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có. Khách nhận tiền bồi thường nhanh (< 5 phút); hãng vận chuyển không bị phạt oan; kế toán (chị Oanh) đối soát khớp sổ không thất thoát quỹ; người duyệt (chị Hạnh) không bị quá tải hàng chờ (SLA < 60 phút). |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu ép tỷ lệ tự động hoàn tiền quá cao mà bỏ lỏng ranh giới đỏ, kế toán (chị Oanh) và LogiX chịu thiệt vì thất thoát dòng tiền do hoàn sai, hãng vận chuyển chịu thiệt vì phạt oan; ngược lại nếu hạ trần chuyển người quá thấp để an toàn thì chị Hạnh và đội ngũ CSKH sẽ bị quá tải, kiệt sức vì ùn ứ ticket. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng. Ngày 1 đặt an toàn tài chính và pháp lý lên hàng đầu (hoàn sai = 0đ, lỗi oan = 0, PII = 0) trong phạm vi thí điểm nhỏ (2 kho HN, HCM), chấp nhận tỷ lệ chuyển người duyệt ở mức an toàn (≤ 25%). |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ở ngày thứ 1.000, trần ngân sách ngày (2.000.000đ) và trần chi phí ticket (8.000đ) sẽ phải viết lại và nâng lên theo quy mô đơn hàng tăng trưởng; chính sách hoàn tiền (REFUND-v4, v5) sẽ thay đổi hạn mức tự động và điều kiện miễn trách nhiệm thiên tai nên logic kiểm tra chính sách phải cập nhật liên tục qua policy engine. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 8000 · `roi_min` 0.2 · `queue_stuck_max` 0
- Ngày xem lại tiêu chí: `2026-12-01` · Ai dự: `Phạm Hoàng Đức Minh (Sản phẩm), Lê Phạm Thành Đạt (Kỹ sư cổng), Nguyễn Ngọc Bách (Vận hành & Pháp lý), chị Oanh (Kế toán), chị Hạnh (CSKH)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-19T15:25:59` |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `4f7f982` |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
