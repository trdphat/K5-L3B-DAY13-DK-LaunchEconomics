# Báo cáo cá nhân — Nguyễn Minh Nhân - 2A202603723

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Nhân
- MSSV: 2A202603723
- Email: 26ai.nhannm@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số (M2), kiêm triển khai code phân tích độ nhạy chi phí.

## 2. Phần việc phụ trách

- CP2 — Nhiệm vụ B1–B4: Phân tích độ nhạy chi phí của trợ lý AI hoàn phí LogiX-VN.
- Triển khai hàm `chay_B()` trong `src/lab13.py`, tái sử dụng hàm `mo_hinh()` của M1.
- Hoàn thiện phần B trong `report/team/bang_chi_phi.md`.
- Kiểm tra công thức, độ chính xác và tính nhất quán của số liệu.
- Phụ trách phân tích rủi ro kinh tế E2 theo phân công nhóm.

## 3. Đóng góp cụ thể

- **B1:** Triển khai 9 kịch bản thay đổi giá token, chi phí xem lại, chi phí làm lại, lương nhân viên và giới hạn số lần chạy.
- **B2:** Phân tích kịch bản kết hợp giá token và chi phí xem lại cùng tăng gấp đôi; xếp hạng ba yếu tố ảnh hưởng mạnh nhất.
- **B3:** So sánh giới hạn chạy lại 1, 2 và 3 lần, phân biệt chi phí mỗi việc thành công với tổng chi phí hệ thống.
- **B4:** Phân tích kịch bản xem lại 100% trong phạm vi `noi_dia` và `hang_nang`, với hai mức làm lại 9 và 15,3 phút/ca; xác định ngưỡng thời gian xem lại hòa vốn.
- Kiểm chứng kết quả tính toán, bảo đảm sai số trong giới hạn 2%.
- Giữ nguyên contract của `mo_hinh()`, dữ liệu CSV, starter code và phần việc của các thành viên khác.

## 4. Bằng chứng

### File đóng góp

| File | Nội dung |
|---|---|
| `src/lab13.py` | Hoàn thiện hàm `chay_B()` |
| `report/team/bang_chi_phi.md` | Hoàn thiện B1–B4 |

### Kết quả tính toán

Toàn bộ số liệu chi phí dưới đây mang nhãn `simulated`.

| Chỉ tiêu | Kết quả |
|---|---:|
| Chi phí cơ sở mỗi việc thành công | 4.472 đ |
| Giá token tăng gấp đôi | 4.723 đ (+5,6%) |
| Xem lại tăng gấp đôi | 6.292 đ (+40,7%) |
| Làm lại tăng gấp đôi | 6.787 đ (+51,8%) |
| Lương tăng 25% | 5.506 đ (+23,1%) |
| Token và xem lại cùng tăng gấp đôi | 6.543 đ (+46,3%) |
| Chi phí hệ thống khi chạy tối đa 1 lần | 7.449.781 đ |
| Chi phí hệ thống khi chạy tối đa 2 lần | 6.901.220 đ |
| Chi phí hệ thống khi chạy tối đa 3 lần | 7.037.585 đ |
| Xem lại 100%, làm lại 9 phút/ca | 11.743 đ |
| Xem lại 100%, làm lại 15,3 phút/ca | 12.415 đ |

Kết quả cho thấy chi phí làm lại và xem lại ảnh hưởng mạnh hơn giá token. Giới hạn 2 lần chạy tối ưu tổng chi phí hệ thống, mặc dù giới hạn 1 lần có chi phí mỗi việc thành công thấp hơn.

### Kết quả kiểm chứng

- Chương trình chạy thành công.
- Ba phép thử A1: ĐẠT.
- B1 hoàn thành đủ 9 kịch bản.
- Sai số tối đa: 0,01496%, thấp hơn ngưỡng 2%.
- B3–B4 khớp phép tính đối chiếu độc lập.
- `git diff --check`: ĐẠT.
- Giữ nguyên chữ ký và 9 key trả về của `mo_hinh()`.


## 5. Công cụ AI đã dùng

**ChatGPT:**

- Hỗ trợ phân tích yêu cầu, phân chia công việc và xác định dependency giữa các thành viên.
- Xây dựng kế hoạch triển khai CP2, viết prompt cho Codex và hướng dẫn sử dụng Git.
- Hỗ trợ tổng hợp báo cáo cá nhân.

**OpenAI Codex:**

- Đọc tài liệu Markdown, source code và rubric của Lab 13.
- Hỗ trợ triển khai hàm `chay_B()` và hoàn thiện bảng chi phí B1–B4.
- Phát hiện yêu cầu bổ sung về hai mức thời gian làm lại và ngưỡng hòa vốn trong B4.
- Chạy chương trình, đối chiếu công thức, kiểm tra sai số và phạm vi thay đổi.

**Kiểm soát kết quả AI:**

Tôi giới hạn phạm vi chỉnh sửa của AI trong hai file được phân công, yêu cầu giữ nguyên contract của M1 và không thay đổi dữ liệu gốc. Tôi sử dụng kết quả chạy chương trình, phép tính đối chiếu và báo cáo kiểm tra của Codex để đánh giá tính chính xác của kết quả.

## 6. Tự đánh giá

Tôi đã hoàn thành CP2, bao gồm toàn bộ nhiệm vụ B1–B4, với kết quả đáp ứng ngưỡng sai số theo yêu cầu.

Qua bài lab, tôi hiểu rõ hơn sự khác biệt giữa chi phí sử dụng mô hình AI, chi phí mỗi việc thành công và tổng chi phí vận hành hệ thống.

Kết quả phân tích cho thấy tối ưu giá token không phải yếu tố quan trọng nhất. Giảm lỗi, thời gian xem lại và chi phí làm lại có thể mang lại hiệu quả kinh tế lớn hơn.

Tôi cũng cải thiện kỹ năng phối hợp nhóm, sử dụng contract chung, phân tích độ nhạy và sử dụng công cụ AI trong quy trình phát triển phần mềm.

Điểm cần cải thiện là tăng khả năng kiểm chứng độc lập kết quả do AI tạo ra và nâng cao kỹ năng đánh giá rủi ro kinh tế trước khi triển khai Pilot.

Phần E2 sẽ được bổ sung sau khi hoàn thành theo phân công nhóm.