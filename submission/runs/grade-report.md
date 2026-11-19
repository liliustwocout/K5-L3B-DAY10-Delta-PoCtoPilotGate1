# Tự kiểm tra sự cố S4 · PASS-VISIBLE (chưa chạy test ẩn)

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S4-grade-20261119-174404-c66ec6` · bàn: `K5-L3B-DAY10-Delta-PoCtoPilotGate1` · grader `lab10-1.0` · 0.445s
- Ba mốc: base `R-S4-before-20261119-174404-c66ec6` · prepared `R-S4-prepared-20261119-174404-c66ec6` · after `R-S4-after-20261119-174404-c66ec6` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `7e724506`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `c66ec63eee11`
- Hash Bản tiêu chí chấp nhận: `4414b7250dbe` · đã ký: `4414b7250dbe` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S4` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S4 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ✅ | file khoá bị đổi: không |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ✅ | base có vấn đề: True; after sạch: True; ticket còn hỏng: không; trần còn vượt: không |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['fail_open_rate', 'max_queue_wait_min', 'max_daily_auto_refund_vnd']; sáng đèn: [('fail_open_rate', 'before', 0.0, 0.185366), ('fail_open_rate', 'after', 0.0, 0.243478), ('max_queue_wait_min', 'before', 0.0, 78.0), ('max_queue_wait_min', 'after', 0.0, 42.0), ('max_daily_auto_refund_vnd', 'before', 155000.0, 466000.0), ('max_daily_auto_refund_vnd', 'after', 155000.0, 248000.0)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.3659 | 0.5043 | 0.5043 |
| thời gian chờ trung bình (phút) | 37.9 | 17.0 | 17.0 |
| thời gian chờ lâu nhất (phút) | 78.0 | 42.0 | 42.0 |
| số ca bị ùn | 4 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4980 · 10000 | 6966 · 10000 | 6966 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 871 · 1500 | 971 · 1500 | 971 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 173822 | 69777 | 69777 |
| ROI | 0.85 | 0.44 | 0.44 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 466000 · 300000 | 248000 · 300000 | 248000 · 300000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 44000 · 300000 | 0 · 300000 | 0 · 300000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.561 | 0.561 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 27 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.975; hoàn sai 0; oan 1; PII 0; chi phí 4216đ | — | — |
| kho DN | pass 0.92; hoàn sai 40000; oan 4; PII 0; chi phí 5562đ | — | — |
| kho HCM | pass 0.8182; hoàn sai 0; oan 10; PII 0; chi phí 3395đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 5784đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 5784đ |
| kho HN | pass 0.8; hoàn sai 120000; oan 12; PII 0; chi phí 3957đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 5550đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 5550đ |
| hãng DNB | pass 0.875; hoàn sai 36000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.8571; hoàn sai 0; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 0.8286; hoàn sai 40000; oan 6; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 0.925; hoàn sai 36000; oan 3; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.8545; hoàn sai 48000; oan 8; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.3077 | 0.3077 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 5550 · 10000 | 5550 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 770 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 57853 | 57853 |
| ROI | 1.34 | 0.8 | 0.8 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.5909 | 0.5909 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | — | — |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | — | — |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3447đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3447đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- Không vượt trần kinh doanh / vận hành nào.
- Mọi ngưỡng đã ký đều đạt.
- Được phép cân nhắc 'Tiếp tục'.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2308 | 0.2308 | +0.0035 |
| visible | pass_rate | 0.8683 | 1.0 | 1.0 | +0.1317 |
| visible | pass_k | 0.6829 | 1.0 | 1.0 | +0.3171 |
| visible | wrongful_refund_vnd | 160000 | 0 | 0 | -160000 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 27 | 0 | 0 | -27 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.3659 | 0.4957 | 0.4957 | +0.1298 |
