# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu có `duoc_xem_lai == 1` | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | 4,25% (51 / 1.200); phạm vi `noi_dia` + `hang_nang`: 3,97% (39 / 982) |
| Dùng (nhóm đề xuất) | Tỉ lệ kích hoạt trợ lý ở nhóm can thiệp | Số yêu cầu thuộc nhóm can thiệp có mở gợi ý trợ lý (`agent_suggestion_shown`), chia tổng yêu cầu nhóm can thiệp (`refund_request_created` với `arm == treatment`) | Không cần tính |
| An toàn (nhóm đề xuất) | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn có `so_tien_da_hoan != so_tien_dung` trong `audit_sample_checked`, chia tổng số đơn được kiểm tra mẫu trong tuần (tối thiểu 100 đơn/tuần) | Không cần tính |

> **Lưu ý diễn giải:** Chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200), tỉ lệ bỏ qua gợi ý là **27,12%** (48/177), và tỉ lệ mở lại trong 7 ngày là **4,25%** (51/1.200). **Không** viết "trợ lý đã nâng chỉ số từ 70%" vì đợt chạy thử 2 tuần không có nhóm đối chứng.

## Danh sách event

Mỗi event đều gắn `trace_id` để nối trực tiếp với trace của agent và đối soát sổ cái.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / cổng CSKH | `request_id`, `loai`, `depot`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `price_table_version`, `trace_id` | Sau mỗi lần chạy agent (kể cả lần lỗi) |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `decision` (`giu`/`sua`/`bo`), `phut_xem_lai` (đo thật), `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai` (đo thật), `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại yêu cầu sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi agent chuyển yêu cầu sang nhân viên xử lý |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi yêu cầu được đóng |
| `ticket_reopened` | App khách / CSKH | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu sau khi đóng |
| `audit_sample_checked` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_vnd`, `trace_id` | Hằng tuần khi kiểm tra mẫu 100 đơn |

**Kiểm tra chéo (event → chỉ số E1):**

- **Chỉ số chính (% đóng trong 24h & không mở lại trong 7 ngày):** ghép theo `trace_id` từ `refund_request_created` (mẫu số, mốc tạo) + `ticket_closed` (`closed_at - created_at <= 24h`) + không có `ticket_reopened` trong vòng 7 ngày sau `closed_at`.
- **Chỉ số dùng (tỉ lệ bỏ qua gợi ý):** tính từ `staff_review_decision` — số bản ghi có `decision in ('sua', 'bo')` chia tổng số bản ghi `staff_review_decision`.
- **Chỉ số an toàn (tỉ lệ mở lại trong 7 ngày):** ghép `refund_request_created` (mẫu số) + `ticket_reopened` có `reopened_at - closed_at <= 7 ngày` (tử số).
- **Chỉ số dùng đề xuất (tỉ lệ kích hoạt trợ lý nhóm can thiệp):** ghép `refund_request_created` lọc `arm == 'treatment'` (mẫu số) + `agent_suggestion_shown` (tử số, theo `trace_id`).
- **Chỉ số an toàn đề xuất (tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu):** tính trực tiếp từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung` chia tổng số đơn được kiểm tra trong tuần).
- **Bổ trợ chi phí & đối soát pilot:** `agent_run_completed` + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai` thay thế các cột `_simulated` bằng số đo thật sau tuần 1; `refund_ledger_write` phát hiện hoàn trùng (ca 7, 20).

## E2 · Rủi ro kinh tế

M2 — Nguyễn Minh Nhân (2A202603723). Nguồn: [A2–A4, B1–B4](bang_chi_phi.md), đối chiếu bằng `chay_A()` và `chay_B()` trong [lab13.py](../../src/lab13.py); số tính trước khi làm tròn. Các chi phí có giờ nhân viên mang nhãn **simulated**.

B1–B3 dùng toàn mẫu 1.200 yêu cầu; A4 và B4 chỉ dùng `noi_dia` + `hang_nang` (982 yêu cầu, 900 việc thành công). B1–B4 chưa cộng cố định; A4 đã cộng 40 triệu đ/tháng; so sánh B4 với 12.000 đ là CPS theo công thức đề, chưa cộng phần nhân viên làm thay như B3.

Các ngưỡng 7%, 50%, 15% và hành động dưới đây là **đề xuất theo hướng dẫn E2**, cần M3/M4 thống nhất trước pilot; không phải kết quả đã quan sát hay luật dừng đã được phê duyệt.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1: CPS 4.472 → **6.787 đ, +51,8% [simulated]**, toàn mẫu 1.200 yêu cầu | Tỉ lệ `lam_lai` trong phạm vi > 7%/tuần; mốc chạy thử 48/982 = 4,9%; đo thêm phút làm lại thực tế | Thu hẹp về `noi_dia`, rà 20 trace làm lại và sửa nguyên nhân trước khi mở lại `hang_nang` | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | B4: **11.743 đ = 0,98×** với làm lại 9 phút; **12.415 đ = 1,03×** với 15,3 phút/ca [simulated], so với 12.000 đ | Tỉ lệ xem lại > 50% cuối bước rollout 0,25; đo phút xem lại/làm lại và tỉ lệ sửa + bỏ | Chỉ giảm xem lại theo bậc khi sửa + bỏ < 15% và đạt ngưỡng an toàn M3 chốt; thiếu bằng chứng thì giữ xem lại và chưa mở rộng | Trưởng nhóm CSKH |
| Khối lượng thấp làm tăng phần cố định mỗi việc | A4: 45.000 → 22.500 yêu cầu/tháng, cố định 1.185 → 2.370 đ/việc; CPS có cố định **4.599 → 5.784 đ [simulated]** | Số việc thành công trong phạm vi theo tuần < 50% kế hoạch tương ứng mức rollout; cập nhật dự báo tháng | Chưa mở rộng pilot; tính lại phân bổ 40 triệu đ/tháng, rà ngân sách và chi phí cố định theo khối lượng mới | PM trợ lý hoàn phí |
| Chọn 1 lần chạy chỉ vì CPS thấp, đẩy việc sang nhân viên | B3: 1 lần có CPS 4.111 đ nhưng hệ thống 7.449.781 đ; 2 lần là **6.901.220 đ**, thấp hơn **548.560 đ [simulated]**, giảm 85 ca không thành công | So sánh chi phí cả hệ thống/yêu cầu và số chuyển nhân viên theo tuần, cùng phạm vi và kỳ đo giữa giới hạn 1 và 2 | Đề xuất giới hạn 2 lần từ B3; tính lại trên phạm vi pilot, bàn giao M3 chốt chính sách chạy lại theo tổng chi phí và an toàn | PM trợ lý hoàn phí |

**Công thức và đối chiếu:**

- **B1:** `CPS = (token + tool + xem_lai + 2 × lam_lai) / 978 = 6.787 đ`; `Δ% = (CPS / CPS_A2 − 1) × 100 = +51,8%` [simulated]. Kịch bản giữ nguyên 978 việc thành công và nhân đôi tiền làm lại; ngưỡng cảnh báo 7% không đồng nghĩa với tăng gấp đôi tỉ lệ làm lại.
- **B4:** `CPS(r) = (224.513 + 948 × 5 × 2.000 + 48 × r × 2.000) / 900`; `r = 9` → 11.743 đ, `r = round(1.132 / 74, 1) = 15,3` → 12.415 đ [simulated]. Đếm 948 request_id có ít nhất 1 run `ok`, mỗi yêu cầu xem lại một lần.
- **Hòa vốn B4:** `t = (12.000 × 900 − token − tool − 48 × r × 2.000) / (948 × 2.000)` → khoảng 5,1 hoặc 4,8 phút xem lại khi `r = 9` hoặc `15,3` [simulated]; dùng số chưa làm tròn để quyết định. Đây là ngưỡng theo CPS của B4.
- **A4:** `CPS_có_cố_định(Q) = CPS_phạm_vi + 40.000.000 / (Q × 900 / 1.200)` → 4.599 đ ở `Q = 45.000`, 5.784 đ ở `Q = 22.500` [simulated]. Giữ nguyên cơ cấu mẫu; lượng thành công tháng là 33.750 hoặc 16.875.
- **B3:** `H(k) = tổng_trợ_lý(k) + 12.000 × (1.200 − thành_công(k))`; `H(1) − H(2) = 548.560 đ [simulated]`, số ca không thành công giảm `319 − 234 = 85`. Kết quả này thuộc toàn mẫu, cần tính lại trước khi áp dụng cho phạm vi pilot.

**Cách đo đề xuất:** tỉ lệ làm lại = số yêu cầu `lam_lai` / tổng yêu cầu trong phạm vi; tỉ lệ xem lại = số yêu cầu được xem / số yêu cầu có ít nhất 1 run `ok`; tỉ lệ sửa + bỏ = số quyết định `sua` hoặc `bo` / số yêu cầu được xem. Đếm theo request_id duy nhất, cùng kỳ; mẫu số bằng 0 thì báo thiếu dữ liệu.

**Kết luận:** ưu tiên kiểm soát làm lại (+51,8%) và xem lại (+40,7%), rồi lương (+23,1%) theo B2 [simulated]; xem lại 100% có thể vượt 12.000 đ ngay cả khi chưa cộng cố định. Pilot cần đo phút thực tế và chứng minh giảm xem lại vẫn an toàn.

**Dependency và bàn giao:**

- **M3:** cần đối chiếu và chốt phạm vi, kế hoạch khối lượng theo rollout, ngưỡng an toàn và luật dừng. E2 đã đủ số để hoàn thành; chưa thể xác nhận các hành động giảm xem lại/chạy lại đã đáp ứng kế hoạch pilot.
- **M4:** E1 và danh sách event đã có trong tài liệu; cần kiểm tra event đo được các tỉ lệ/phút ở E2, có trace_id để nối trace, rồi tổng hợp 4 rủi ro vào mục 7 E3. Khi dẫn chi phí và rủi ro sang E3, ghi trạng thái **Giả lập** và giữ nhãn simulated.

**Đối chiếu rubric:** theo [hướng dẫn E2](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) và [rubric C5](../../RUBRIC.md), E2 có 4 dòng (yêu cầu ít nhất 2), đủ 5 cột, nguồn số và công thức; hỗ trợ bằng chứng C6/C7. C5 có 10 điểm cho toàn nhiệm vụ E; phần chỉ số/event E1 và hồ sơ 7 mục E3 vẫn do M4 hoàn thiện.
