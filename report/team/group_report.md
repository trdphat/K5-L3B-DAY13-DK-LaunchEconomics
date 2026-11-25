# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: DK
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ **hồ sơ launch v0** trình hội đồng **Gate 2a** cho trợ lý hoàn phí của LogiX-VN (dữ liệu giả lập 1.200 yêu cầu, 1.624 lần chạy) nhằm trả lời bốn câu hỏi: (1) có đáng chạy về mặt kinh tế không, (2) nhân viên có sử dụng và đo được bằng event không, (3) khi lỗi thì phân loại và khắc phục ra sao, (4) thiết kế pilot thế nào để tách được tác động và ra quyết định rõ ràng.

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí):** Kiểm chứng 3 phép thử A1 (`1,20 · 1,25 · 1,25`), xây dựng `mo_hinh()` trong `src/lab13.py` tính đủ token + tool (mọi lần chạy kể cả lỗi) và giờ nhân viên xem lại/làm lại (`simulated`), tách theo 4 loại yêu cầu và cộng chi phí cố định 40 triệu đ/tháng → [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (Độ nhạy):** Chạy 9 kịch bản đổi từng yếu tố, 1 kịch bản đổi cặp, so sánh chi phí cả hệ thống ở giới hạn 1/2/3 lần chạy và kịch bản xem lại 100% → [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Phân loại lỗi):** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đối chiếu đồng thuận và lập bảng phát hiện/khắc phục cho 5 ca đại diện → [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính cỡ mẫu hiệu dụng cho 3 cách chia, chọn chia ngẫu nhiên theo nhân viên 20 + 20 cụm (chấp nhận MDE 6 điểm), viết đủ 3 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ → [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, rủi ro & hồ sơ launch v0):** Tính thử 3 chỉ số, đề xuất 2 chỉ số mới, thiết kế 10 event có `trace_id`, tổng hợp rủi ro kinh tế → [chi_so.md](chi_so.md) và gói gọn 7 mục thành 1 trang quyết định → [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Kinh tế (`simulated`):** Chi phí mỗi việc thành công toàn mẫu **4.472 đ** (gấp 16,3× hoá đơn token+tool 274,7 đ/yc); chi phí cả hệ thống **5.865 đ/yc = 0,49×** so với nhân viên tự làm (12.000 đ). Trong phạm vi pilot `noi_dia` + `hang_nang`: **3.414 đ** (cộng cố định thành **4.599 đ** ở quy mô đầy đủ hoặc **5.784 đ** ở 50% khối lượng). Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%). Xem lại 100% làm chi phí tăng lên **11.743–12.414 đ** (`0,98×–1,03×`, `simulated`).
- **Chỉ số đợt chạy thử (chưa có đối chứng):** Chính **82,83%** (994/1.200); Dùng (bỏ qua gợi ý) **27,12%** (48/177); An toàn (mở lại 7 ngày) **4,25%** (51/1.200).
- **Đề xuất Gate 2a:** **Go có điều kiện** cho pilot `noi_dia` + `hang_nang` (giới hạn 2 lần chạy) với 4 điều kiện cụ thể về khoá chống trùng sổ cái, đo thật thay cho `simulated`, lộ trình giảm xem lại và ký chấp nhận MDE 6 điểm.
- **Kết quả duyệt chéo Gate 2a:** *(Cập nhật sau phiên duyệt chéo 17:00 tại lớp; phiếu nhóm chấm nhóm khác lưu tại [phieu_cham.md](phieu_cham.md)).*

## 5. Khó khăn và cách xử lý

- **Chi phí ẩn từ giờ nhân viên:** Giờ xem lại và làm lại chiếm 92,5% tổng chi phí (`simulated`), nên nhóm kiểm tra chéo cả chi phí cả hệ thống (B3) và kịch bản xem lại 100% (B4) thay vì chỉ nhìn hoá đơn token.
- **Giới hạn cỡ mẫu với 40 nhân viên:** Không cách chia theo cụm nào đủ mẫu cho MDE 5 điểm (tối đa 1.000 < 1.251). Nhóm chọn 20 + 20 nhân viên, chấp nhận MDE 6 điểm (`m ≥ 299`) và ghi rõ power chỉ còn 0,64 ở mức 5 điểm.
- **Làm việc phân tán (có thành viên làm từ xa):** Chia nhánh Git độc lập theo 4 vai (`feat/cost-model`, `feat/sensitivity-analysis`, `feat/evaluation-pilot`, `feat/metrics-launch`) và phân quyền rõ từng vùng file để tránh conflict.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và các file báo cáo cá nhân `report/team/MSSV_HoTen.md`.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Thời gian xem lại và làm lại hiện là số `simulated`; đợt chạy thử chưa có nhóm đối chứng nên chưa kết luận được tác động nhân quả; chọn MDE 6 điểm làm giảm power xuống 0,64 nếu tác động thật là 5 điểm.
- **Hướng cải thiện:** Thay toàn bộ số `simulated` bằng log thời gian thật (`staff_review_decision`, `staff_rework_completed`) ngay sau tuần 1 pilot; bổ sung kiểm tra mẫu hằng tuần (`audit_sample_checked`) để phát hiện sớm lỗi ngầm.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook* — chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu `statsmodels` (`NormalIndPower`, mục `stats.power`) và tài liệu đề bài Lab 13 (`docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`).
