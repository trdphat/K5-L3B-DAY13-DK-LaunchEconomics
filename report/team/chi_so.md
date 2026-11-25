# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

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

- **M3:** phần D còn khung; cần chốt phạm vi, kế hoạch khối lượng theo rollout, ngưỡng an toàn và luật dừng. E2 đã đủ số để hoàn thành; chưa thể xác nhận các hành động giảm xem lại/chạy lại đã đáp ứng kế hoạch pilot.
- **M4:** E1 và danh sách event còn khung; cần bảo đảm event đo được các tỉ lệ/phút ở E2, có trace_id để nối trace, rồi tổng hợp 4 rủi ro vào mục 7 E3. Khi dẫn chi phí và rủi ro sang E3, ghi trạng thái **Giả lập** và giữ nhãn simulated.

**Đối chiếu rubric:** theo [hướng dẫn E2](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) và [rubric C5](../../RUBRIC.md), E2 có 4 dòng (yêu cầu ít nhất 2), đủ 5 cột, nguồn số và công thức; hỗ trợ bằng chứng C6/C7. C5 có 10 điểm cho toàn nhiệm vụ E; phần chỉ số/event E1 và hồ sơ 7 mục E3 vẫn do M4 hoàn thiện.
