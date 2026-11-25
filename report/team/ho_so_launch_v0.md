# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: DK · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: **4.472 đ** (`simulated`), gấp 16,3× hoá đơn token+tool (274,7 đ/yc). Phạm vi pilot `noi_dia` + `hang_nang`: **3.414 đ** (`simulated`); cộng cố định 40 triệu đ/tháng thành **4.599 đ** (quy mô đầy đủ) hoặc **5.784 đ** (50% khối lượng pilot, `simulated`). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1) Số ca làm lại gấp đôi: **+51,8%** lên 6.787 đ; 2) Tỉ lệ xem lại gấp đôi: **+40,7%** lên 6.292 đ; 3) Lương nhân viên tăng 25%: **+23,1%** lên 5.506 đ (đều `simulated`). Giá token gấp đôi chỉ tăng **+5,6%**. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Nhân viên tự làm: 12.000 đ/yc. Chi phí cả hệ thống (đã cộng phần chuyển nhân viên): **5.865 đ/yc = 0,49×** (`simulated`). Theo loại: `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` 1,88× (`simulated`) → loại `quoc_te` và `doi_tac` khỏi pilot. | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (chưa có đối chứng): Chính **82,83%** (994/1.200); Dùng (bỏ qua gợi ý) **27,12%** (48/177); An toàn (mở lại 7 ngày) **4,25%** (51/1.200; trong phạm vi pilot 3,97%). Đủ 10 event có `trace_id`. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi gắn nhãn độc lập bởi M3 và M4 theo 5 loại Google PAIR, đồng thuận **20/20 = 100%**; 5 ca đại diện đủ 5 loại có cơ chế phát hiện đo được (event, ngưỡng, tần suất) và vai trò phụ trách riêng (ưu tiên khoá chống trùng ca 7, 20 và kiểm tra mẫu 100 đơn/tuần ca 17). | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chỉ chạy `noi_dia` + `hang_nang`; chia ngẫu nhiên theo nhân viên **20 + 20 cụm** (phân tầng theo depot); rollout `10% → 25% → 50%`; MDE chấp nhận **6 điểm** (`n_hiệu_dụng = 859`, `m ≥ 299`, `DE = 6,96`, power ở mức 5 điểm còn **0,64**); 3 luật dừng đủ 4 vế (ngưỡng chi phí 6.708 đ/việc, `simulated`); rollback 30 phút; ngày quyết định `2027-01-15`. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Tổng hợp 4 rủi ro từ E2 (`simulated`): (1) Làm lại gấp đôi: **4.472 → 6.787 đ (+51,8%)**; (2) Xem lại 100% kéo dài: **11.743 đ = 0,98×** (9 phút) hoặc **12.415 đ = 1,03×** (15,3 phút/ca, hòa vốn ≤ 5,1 hoặc 4,8 phút xem lại); (3) Khối lượng giảm một nửa (45.000 → 22.500 yc/tháng): cố định tăng 1.185 → 2.370 đ, CPS có cố định **4.599 → 5.784 đ**; (4) Giới hạn 1 lần chỉ vì CPS thấp (4.111 đ) đẩy thêm 85 ca sang nhân viên, làm tổng hệ thống tăng **+548.560 đ** so với 2 lần (**6.901.220 đ**). | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** — chỉ phê duyệt kế hoạch pilot cho phạm vi `noi_dia` + `hang_nang` (giới hạn tối đa 2 lần chạy/yêu cầu để tối ưu chi phí cả hệ thống 6.901.220 đ, `simulated`), với 4 điều kiện bắt buộc trước và trong tuần đầu pilot:

- **Điều kiện 1 (An toàn sổ cái):** Bổ sung khoá chống trùng (`idempotency_key`) và chỉ báo "đã hoàn" khi sổ cái trả `ok` (khắc phục ca 7, 20) — **Phụ trách:** Kỹ sư trưởng agent · **Ngày kiểm tra:** trước ngày mở bước `0.10`.
- **Điều kiện 2 (Đo thật thay cho `simulated`):** Bật đủ 10 event có `trace_id`, đo trực tiếp `phut_xem_lai` và `phut_lam_lai` từ log, tính lại chi phí thật sau tuần 1 — **Phụ trách:** PM trợ lý hoàn phí · **Ngày kiểm tra:** cuối tuần 1 pilot.
- **Điều kiện 3 (Giảm xem lại theo bậc):** Chốt lộ trình hạ tỉ lệ xem lại xuống dưới 50% trước khi hết bước `0.25` (vì xem lại 100% tốn 0,98×–1,03×, `simulated`, không tiết kiệm) — **Phụ trách:** Trưởng nhóm CSKH · **Ngày kiểm tra:** cuối bước `0.25`.
- **Điều kiện 4 (Chấp nhận đánh đổi cỡ mẫu):** Ký xác nhận chấp nhận MDE 6 điểm (power 0,64 nếu tác động thật chỉ 5 điểm) do giới hạn 40 nhân viên — **Phụ trách:** Giám đốc vận hành LogiX-VN · **Ngày kiểm tra:** trước ngày bốc thăm chia nhóm.
