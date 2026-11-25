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

Số lấy trực tiếp từ bảng độ nhạy và chi phí cố định (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, tăng từ 4.472 đ lên **6.787 đ/việc** (`simulated`) | Tỉ lệ ca `lam_lai` theo tuần vượt 7% (đợt chạy thử: 48/982 = 4,9% trong phạm vi `noi_dia` + `hang_nang`) | Thu hẹp phạm vi về `noi_dia`, rà 20 trace `staff_rework_completed` gần nhất để sửa lỗi gốc | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ = 0,98×** (9 phút làm lại) hoặc **12.415 đ = 1,03×** (15,3 phút theo dữ liệu, `simulated`) — không tiết kiệm hoặc đắt hơn nhân viên tự làm | Tỉ lệ yêu cầu có `staff_review_decision` vẫn > 50% ở cuối bước rollout `0.25`, hoặc phút xem lại trung bình > 4,8 phút | Áp dụng lộ trình giảm xem lại theo bậc khi tỉ lệ bỏ qua gợi ý (`sua` + `bo`) < 15% và rà giao diện để rút ngắn thời gian xem lại | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng tăng từ **+1.185 đ/việc** (45.000 yc/tháng → 4.599 đ) lên **+2.370 đ/việc** khi khối lượng giảm một nửa (→ 5.784 đ, `simulated`) | Số việc thành công mỗi tuần thấp hơn 50% kế hoạch trong 2 tuần liên tiếp | Tạm dừng mở rộng quy mô pilot và đàm phán lại cấu trúc chi phí cố định | Giám đốc vận hành LogiX-VN |
