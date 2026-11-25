# Báo cáo cá nhân — TruongDucPhat-2A202603757

## 1. Thông tin thành viên

- Họ tên: Trương Đức Phát
- MSSV: 2A202603757
- Email:
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code (trước giải lao), phụ trách mô hình chi phí (Member 1)

## 2. Phần việc phụ trách

- Khung `src/lab13.py` và contract dùng chung cho cả nhóm: hàm `mo_hinh()` và các hàm vùng `chay_A`, `chay_B`, `chay_D`, `chay_E`.
- Nhiệm vụ A (CP1): A1 ba phép thử, A2 mô hình chi phí từ trace, A3 tách theo loại yêu cầu, A4 chi phí cố định.
- Phần A1–A4 trong `report/team/bang_chi_phi.md`.
- Phiếu chấm hội đồng Gate 2a `report/team/phieu_cham.md` (điền khi duyệt chéo tại lớp).

## 3. Đóng góp cụ thể

- Viết ba hàm A1 theo công thức E = (1 − (1 − p)^k) ÷ p, P = 1 − (1 − p)^k, hệ số = E ÷ P; k = None là chạy đến khi đúng (E = 1/p, P = 1).
- Viết `mo_hinh(runs, reqs, …)` trả đúng 9 key `token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc`; tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`; hỗ trợ tham số giá, hệ số xem lại/làm lại và `max_lan_chay` để M2 gọi lại ở nhiệm vụ B.
- Chia `lab13.py` thành vùng của từng người (B: M2, D: M3, E: M4) để giảm conflict; phần B, D, E chỉ để stub cho người phụ trách.
- Kết quả chính: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn 274,7 đ; làm lại chiếm 51,8% [simulated]; quoc_te 22.515 đ = 1,88× [simulated] và chạy lại không giúp (ok 30,0% → 11,4% → 2,2%); phạm vi noi_dia + hang_nang cộng cố định 4.599 đ = 0,38× [simulated].

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- File: `src/lab13.py` (vùng chung, A1, `mo_hinh`, `chay_A`), `report/team/bang_chi_phi.md` (mục A1–A4).
- Output: `cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và các bảng A2, A3, A4.
- Commit: ghi hash sau khi nhóm merge nhánh của M1.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Claude Code (Claude): đọc tài liệu repo, lập kế hoạch phân công 4 thành viên, viết code A1–A4 và `mo_hinh`, điền bảng A1–A4.
- Cách kiểm tra:
  - Ba assert có sẵn trong `kiem_tra_dap_an_biet_truoc()` đều đạt; không sửa assert.
  - Đối chiếu từng con số A2, A3, A4 với số tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`: tất cả lệch dưới 2% (chỗ lệch lớn nhất là do đáp án đã làm tròn, ví dụ 2/93 = 2,15% so với "2,2%").
  - Kiểm tra `mo_hinh` trả đúng 9 key, không sửa `runs`/`reqs` đầu vào, và tham số `max_lan_chay`, giá token, hệ số làm lại cho đúng số mà nhiệm vụ B cần (4.237 · 4.111 · 4.723 · 6.787 đ).
  - Không có số nào được gõ tay vào code: mọi bảng in ra từ dữ liệu CSV.

## 6. Tự đánh giá

- Nhiệm vụ A đạt điều kiện "Xong khi": ba phép thử đạt, bảng A2 đủ 9 dòng có nhãn simulated, bảng A3 đủ 4 dòng, A4 đủ 2 dòng.
- Phiếu chấm Gate 2a chưa điền: chờ hồ sơ của nhóm được phân công chấm tại buổi duyệt chéo.
