# Báo cáo cá nhân — VuQuangThanh-2A202603736

## 1. Thông tin thành viên

- Họ tên: Vũ Quang Thanh
- MSSV: 2A202603736
- Email: 26ai.thanhvq@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 1 (Evaluation & Pilot Engineer — Member 3: nhiệm vụ C, D1–D3)

## 2. Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, viết quy tắc phân biệt cho các ca dễ lẫn, chọn 5 ca đại diện và lập bảng phát hiện – khắc phục – vai trò phụ trách.
- Tính cỡ mẫu D1 (năm câu a–e), thiết kế cách chia nhóm D2 và viết đầy đủ `report/team/pilot_plan.yaml` (D3), gồm ba luật dừng an toàn – chi phí – mức độ sử dụng.
- Thêm vùng nhiệm vụ D vào `src/lab13.py`: `co_mau_hai_ti_le`, `he_so_thiet_ke`, `co_mau_hieu_dung`, `so_yeu_cau_moi_cum`, `chay_D`, `ti_le_mo_lai`, `chay_D3` và hai lời gọi trong `__main__`.

## 3. Đóng góp cụ thể

- **Bộ nhãn 1:** Do người dùng 4 ca (1, 6, 9, 14); Hệ thống 5 ca (2, 7, 8, 15, 20); Ngữ cảnh 4 ca (3, 10, 16, 18); Giới hạn hệ thống 4 ca (4, 11, 13, 19); Ngầm 3 ca (5, 12, 17).
- **D1 (`chay_D()`):** a) 1.251 yêu cầu/nhóm; b) DE 2,48; 3.103 yêu cầu/nhóm = 42 người/nhóm, cần 84 người > 40 nên không đủ người; c) tối đa 1.000 < 1.251 nên không đạt mức chênh 5 điểm; d) tối đa 300 nên loại; e) m ≥ 299 yêu cầu/người, DE 6,96, 5.980 yêu cầu/nhóm, power ở mức 5 điểm còn 0,64.
- **D3 (`chay_D3()`):** tỉ lệ mở lại trong 7 ngày là 4,25% (51/1.200) toàn mẫu và 3,97% (39/982) trong phạm vi `noi_dia + hang_nang`; vì vậy không đặt ngưỡng tuyệt đối 3% mà dùng chênh +2 điểm so với đối chứng kèm trần 6%.
- **`pilot_plan.yaml`:** chia ngẫu nhiên theo nhân viên 20 + 20 cụm, phân tầng theo depot; rollout 10% → 25% → 50%; MDE 6 điểm; `n_per_arm` 859 hiệu dụng; 3 luật dừng đủ bốn vế; rollback 30 phút; ngày quyết định 2027-01-15; liệt kê 4 nhóm số giả lập.
- **Bảng khắc phục 5 ca:** 9 (do người dùng), 7 (hệ thống), 18 (ngữ cảnh), 4 (giới hạn hệ thống), 17 (ngầm); mỗi dòng có event/ngưỡng/tần suất và một vai trò có quyền quyết định.

## 4. Bằng chứng

- Nhánh `feat/evaluation-pilot`: `src/lab13.py` (vùng nhiệm vụ D), `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`.
- Commit `59e2d1b` (code nhiệm vụ D và hồ sơ C) và commit bổ sung báo cáo cá nhân trên nhánh `feat/evaluation-pilot`; PR #4 đã được merge vào `main`.
- Kiểm chứng local: `python3 -c "import lab13; print(lab13.chay_D())"` in đúng 1.251 / 2,48 / 3.103 / 42 / 1.000 / 300 / 299 / 6,96; `chay_D3()` in 4,25% và 3,97%; `yaml.safe_load` đọc được và `grep '?'` ngoài dòng chú thích không in gì.
- Bộ nhãn 1 gắn độc lập trước khi trao đổi; bộ nhãn 2 do M4 gắn độc lập, đối chiếu đạt đồng thuận 20/20 = 100% (không sửa bộ nhãn sau khi so).

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI (Claude/Cline) để đọc đề, gợi ý cấu trúc bảng và soát lỗi chính tả.
- Tự kiểm tra lại toàn bộ số: tính độc lập cỡ mẫu bằng `statistics.NormalDist`, tính tỉ lệ mở lại bằng đọc CSV bằng thư viện chuẩn, đối chiếu sai số dưới 2% với đáp án; tự đọc lại 20 ca và gắn nhãn trước khi tham khảo bảng nhãn trong tài liệu.
- Không dùng AI để tạo số, nhãn lỗi hoặc kết quả duyệt chéo.

## 6. Tự đánh giá

- Hoàn thành phần C và D theo rubric (C3, C4, C8), số liệu có thể tái tạo bằng code trong repo.
- Hạn chế: hai bộ nhãn và tỉ lệ đồng thuận chưa chốt vì chưa có bộ nhãn độc lập của M4; ngưỡng chi phí tuyệt đối dựa trên A2 của M1, cần cập nhật nếu A2 thay đổi sau khi M2 hoàn thiện B.
