# Team

## Thông tin nhóm

- Tên nhóm: DK
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-DK-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/trdphat/K5-L3B-DAY13-DK-LaunchEconomics` · nhánh `main` · *(điền mã commit chốt trước khi nộp)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Trương Đức Phát | 2A202603757 |  26ai.phattd@vinuni.edu.vn     | trdphat | Người viết code (Cost Model Engineer — A1–A4, chấm chéo) |
|   2 | Nguyễn Minh Nhân | 2A202603723 | 26ai.nhannm@vinuni.edu.vn | uscalurn       | Người kiểm số (Cost & Risk Analyst — B1–B4, E2, QA số liệu) |
|   3 | Vũ Quang Thanh | 2A202603736 | quangthanh2252@gmail.com |        | Người gắn nhãn 1 (Evaluation & Pilot Engineer — C, D1–D3) |
|   4 | Hồ An Lộc | 2A202603743 |       |        | Người gắn nhãn 2 kiêm giữ hồ sơ (Metrics & Launch Engineer — E1, E3, tích hợp) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## TruongDucPhat-2A202603757

### Phần việc phụ trách

- Người viết code trước giải lao (Member 1 — Cost Model Engineer): khung `src/lab13.py` và contract dùng chung `mo_hinh()` cho cả nhóm.
- Nhiệm vụ A (CP1): A1 ba phép thử, A2 mô hình chi phí từ trace, A3 tách theo loại yêu cầu, A4 chi phí cố định; phần A1–A4 trong `report/team/bang_chi_phi.md`.
- Phiếu chấm hội đồng Gate 2a (`report/team/phieu_cham.md`) khi nhóm làm hội đồng cho nhóm khác.

### Đóng góp cụ thể

- Viết ba hàm A1; `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` (1,20 · 1,25 · 1,25).
- Viết `mo_hinh(runs, reqs, …)` trả đúng 9 key (`token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc`), tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`; tham số giá, hệ số và `max_lan_chay` được M2 gọi lại cho B1–B4.
- Chia `lab13.py` thành vùng `chay_A` (M1), `chay_B` (M2), `chay_D` (M3), `chay_E` (M4) để làm song song, không sửa chồng code của nhau.
- Kết quả A: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu; làm lại chiếm 51,8% [simulated]; cả hệ thống 5.865 đ/yêu cầu = 0,49× [simulated]; quoc_te 22.515 đ = 1,88× [simulated] và chạy lại không giúp (ok 30,0% → 11,4% → 2,2%); phạm vi noi_dia + hang_nang cộng cố định 4.599 đ = 0,38× (5.784 đ = 0,48× ở nửa khối lượng) [simulated].
- Rà soát `main` trước khi nộp, báo cho nhóm các chỗ thiếu (báo cáo cá nhân M1 bị xoá, E1 chưa in từ `lab13.py`, mâu thuẫn đồng thuận nhãn giữa `bang_loi.md` và hồ sơ) và khôi phục báo cáo cá nhân của M1.
- Chủ trì chấm chéo Gate 2a và điền `report/team/phieu_cham.md`.

### Bằng chứng

- Commit `1f805dd` (khung code, A1–A4, `bang_chi_phi.md` mục A), merge vào `main` qua PR #2 (`5abf243`).
- Commit `b804c0a` khôi phục `report/team/2A202603757_TruongDucPhat.md`, merge qua PR #6 (`a1bfb5c`).
- Output `cd src && python lab13.py`: mục A2, A3, A4; báo cáo cá nhân `report/team/2A202603757_TruongDucPhat.md`.

## HoAnLoc-2A202603743

### Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi (Nhiệm vụ C, phối hợp đối chiếu với Member 3).
- Thiết kế bộ chỉ số E1, danh sách 10 tracking events có `trace_id` và kiểm tra chéo (`report/team/chi_so.md`, hàm `tinh_chi_so_e1` trong `src/lab13.py`).
- Tổng hợp hồ sơ Launch v0 (`report/team/ho_so_launch_v0.md`) và báo cáo nhóm (`report/team/group_report.md`).

### Đóng góp cụ thể

- Tính thử 3 chỉ số E1 trực tiếp trên 1.200 yêu cầu của `src/logix_requests.csv` (`keep_default_na=False`): Chính 82,83% (994/1.200), Dùng 27,12% (48/177), An toàn 4,25% (51/1.200); đề xuất thêm 2 chỉ số Dùng và An toàn.
- Xây dựng bảng 10 event có `trace_id` và ánh xạ kiểm tra chéo từ event sang từng chỉ số E1.
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR.
- Hoàn thiện 7 mục hồ sơ Launch v0 với đề xuất Go có điều kiện (4 điều kiện có người phụ trách và mốc kiểm tra rõ ràng) và tổng hợp báo cáo nhóm.

### Bằng chứng

- Nhánh `feat/metrics-launch`: `src/lab13.py` (hàm `tinh_chi_so_e1`), `report/team/chi_so.md` (phần E1 & danh sách event), `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/2A202603743_HoAnLoc.md`.

## NguyenMinhNhan-2A202603723

### Phần việc phụ trách

- Thực hiện phân tích độ nhạy chi phí B1–B4 trong `src/lab13.py` và `report/team/bang_chi_phi.md`.
- Phân tích rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- Đảm nhiệm vai trò người kiểm số (Cost & Risk Analyst), đối chiếu công thức, số liệu và kiểm tra tính nhất quán giữa code, bảng chi phí và hồ sơ Launch v0.
- Kiểm tra kết quả tích hợp và chạy thử toàn bộ chương trình Lab 13.

### Đóng góp cụ thể

- **B1:** Phân tích 9 kịch bản thay đổi chi phí, xác định chi phí làm lại có tác động lớn nhất (+51,8%).
- **B2:** Phân tích kịch bản kết hợp giá token và tỉ lệ xem lại tăng gấp đôi (+46,3%); xác định ba yếu tố nhạy nhất: làm lại (+51,8%), xem lại (+40,7%) và lương nhân viên (+23,1%).
- **B3:** Xác định giới hạn 2 lần chạy giúp tối ưu chi phí cả hệ thống (6.901.220 đ), giảm 85 yêu cầu cần nhân viên xử lý so với giới hạn 1 lần.
- **B4:** Tính chi phí khi xem lại 100% (11.743 đ và 12.415 đ/việc), xác định ngưỡng thời gian xem lại hòa vốn tương ứng.
- **E2:** Xây dựng bảng 4 rủi ro kinh tế, đầy đủ tác động định lượng, dấu hiệu theo dõi, hành động khắc phục, vai trò phụ trách và công thức đối chiếu; phân biệt rõ chi phí cố định, chi phí biến đổi và số liệu `simulated`.
- Đối chiếu số liệu giữa `bang_chi_phi.md`, `chi_so.md` và `ho_so_launch_v0.md`; xử lý merge conflict phần E2, bảo toàn E1 và danh sách event của M4.
- Chạy thành công toàn bộ `src/lab13.py`, xác nhận ba phép thử A1 đạt và kết quả tính toán A, B, D, E1 khớp với báo cáo.

### Bằng chứng
- Nhánh `feat/sensitivity-analysis`: `src/lab13.py`
  (hàm `chay_B`, B1–B4), `report/team/bang_chi_phi.md`
  (B1–B4), `report/team/chi_so.md` (E2).
- Đối chiếu số liệu kinh tế trong
  `report/team/ho_so_launch_v0.md`.
- Chạy thành công toàn bộ `src/lab13.py`,
  kết quả tính toán khớp với báo cáo.
- `report/team/2A202603723_NguyenMinhNhan.md`.
