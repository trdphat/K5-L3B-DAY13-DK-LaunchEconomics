# Team

## Thông tin nhóm

- Tên nhóm: DK
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-DK-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/trdphat/K5-L3B-DAY13-DK-LaunchEconomics` · nhánh `main` · *(điền mã commit chốt trước khi nộp)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |        |      |       |        |         |
|   2 |        |      |       |        |         |
|   3 |        |      |       |        |         |
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
