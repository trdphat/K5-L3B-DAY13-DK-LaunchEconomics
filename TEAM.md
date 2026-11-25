# Team

## Thông tin nhóm

- Tên nhóm: DK
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-DK-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/trdphat/K5-L3B-DAY13-DK-LaunchEconomics` · nhánh `main` · *(điền mã commit chốt trước khi nộp)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Trương Đức Phát | 2A202603757 |       | trdphat | Người viết code (Cost Model Engineer — A1–A4, chấm chéo) |
|   2 | Nguyễn Minh Nhân | 2A202603723 | 26ai.nhannm@vinuni.edu.vn |        | Người kiểm số (Cost & Risk Analyst — B1–B4, E2, QA số liệu) |
|   3 | Vũ Quang Thanh | 2A202603736 | 26ai.thanhvq@vinuni.edu.vn | thanhvu101 | Người gắn nhãn 1 (Evaluation & Pilot Engineer — C, D1–D3) |
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

## VuQuangThanh-2A202603736

### Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đối chiếu với Member 4 và chốt nhãn thống nhất (Nhiệm vụ C).
- Phân tích nguyên nhân gốc, viết quy tắc phân biệt cho các ca dễ lẫn, lập bảng khắc phục 5 ca đủ 5 loại với cách phát hiện đo được và một vai trò phụ trách.
- Thiết kế pilot D1–D3: tính cỡ mẫu, chọn cách chia nhóm, viết `report/team/pilot_plan.yaml` và thêm vùng nhiệm vụ D vào `src/lab13.py`.

### Đóng góp cụ thể

- Bộ nhãn 1: Do người dùng 4 ca (1, 6, 9, 14); Hệ thống 5 ca (2, 7, 8, 15, 20); Ngữ cảnh 4 ca (3, 10, 16, 18); Giới hạn hệ thống 4 ca (4, 11, 13, 19); Ngầm 3 ca (5, 12, 17); đối chiếu với bộ nhãn của M4 đạt **20/20 = 100%**.
- D1: 1.251 yêu cầu/nhóm; DE 2,48 → 3.103 yêu cầu/nhóm = 42 người/nhóm (cần 84 > 40 nên không đủ người); 20 nhân viên/nhóm tối đa 1.000 < 1.251 nên không đạt mức chênh 5 điểm; 6 depot/nhóm tối đa 300 nên loại; mức chênh 6 điểm cần m ≥ 299 yêu cầu/người, DE 6,96, 5.980 yêu cầu/nhóm, power ở mức 5 điểm còn 0,64.
- D3: tỉ lệ mở lại trong 7 ngày là 4,25% (51/1.200) toàn mẫu và 3,97% (39/982) trong phạm vi `noi_dia + hang_nang`; chọn ngưỡng chênh +2 điểm so với đối chứng kèm trần 6% thay vì ngưỡng tuyệt đối 3% (sẽ dừng pilot ngay tuần đầu).
- Pilot plan: chia ngẫu nhiên theo nhân viên 20 + 20 cụm, phân tầng theo depot; MDE 6 điểm; 3 luật dừng đủ bốn vế NẾU–TRONG–THÌ–KHÔNG THÌ (ngưỡng chi phí 6.708 đ/việc); rollback 30 phút; ngày quyết định 2027-01-15.
- Code trong `src/lab13.py`: `co_mau_hai_ti_le`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `so_yeu_cau_moi_cum`, `chay_D`, `ti_le_mo_lai`, `chay_D3`.

### Bằng chứng

- Nhánh `feat/evaluation-pilot` (PR #4 đã merge): `src/lab13.py` (vùng nhiệm vụ D), `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/2A202603736_VuQuangThanh.md`.
- PR #10: dọn ghi chú còn chờ trong `bang_loi.md` và cập nhật bằng chứng trong báo cáo cá nhân.
- Kiểm chứng: `cd src && .venv/bin/python lab13.py` exit 0 và in “Ba phép thử đáp án biết trước: ĐẠT”; `yaml.safe_load` đọc được `pilot_plan.yaml` và không còn dấu `?` ngoài dòng chú thích.
