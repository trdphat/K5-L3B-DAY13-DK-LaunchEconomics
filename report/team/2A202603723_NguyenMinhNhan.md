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
- **E2:** Hoàn thiện 4 rủi ro kinh tế trong section E2 của `report/team/chi_so.md`: làm lại tăng, xem lại 100%, khối lượng thấp và tối ưu sai chi phí khi giới hạn chạy lại.
- Ghi tác động, công thức, nguồn A/B, dấu hiệu theo dõi, hành động và vai trò phụ trách; phân biệt số toàn mẫu 1.200 yêu cầu với phạm vi pilot 982 yêu cầu và các ngưỡng đề xuất.
- Kiểm tra dependency với M3/M4, chuẩn bị số liệu và lưu ý để M4 tổng hợp E3; chưa sửa nhiệm vụ D, E1 hoặc E3.

## 4. Bằng chứng

### File đóng góp

| File | Nội dung |
|---|---|
| `src/lab13.py` | Hoàn thiện hàm `chay_B()` |
| `report/team/bang_chi_phi.md` | Hoàn thiện B1–B4 |
| `report/team/chi_so.md` — chỉ section E2 | 4 rủi ro kinh tế, công thức và nguồn số liệu; đề xuất theo dõi, xử lý và bàn giao M3/M4 |

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

### E2 · Kết quả và bằng chứng bổ sung

Nguồn chi tiết: [E2 trong chi_so.md](chi_so.md#e2--rủi-ro-kinh-tế), dùng kết quả [A1–A4, B1–B4](bang_chi_phi.md) đã đối chiếu lại với `src/lab13.py`. Các kết quả chi phí dưới đây là **simulated**.

| Rủi ro | Kết quả đã kiểm chứng |
|---|---|
| Làm lại tăng gấp đôi — B1 | 6.787 đ/việc, +51,8% [simulated]; mốc làm lại trong phạm vi 48/982 = 4,9% |
| Xem lại 100% — B4 | 11.743 đ = 0,98× với 9 phút làm lại; 12.415 đ = 1,03× với 15,3 phút [simulated]; hòa vốn khoảng 5,1 hoặc 4,8 phút xem lại [simulated] |
| Khối lượng giảm một nửa — A4 | 45.000 → 22.500 yêu cầu/tháng; CPS gồm cố định 4.599 → 5.784 đ [simulated] |
| Chọn giới hạn 1 thay vì 2 — B3 | Chi phí hệ thống tăng 548.560 đ [simulated] và thêm 85 ca không thành công trên 1.200 yêu cầu |

**Phương pháp kiểm chứng E2 đã thực hiện:**

- Chạy lại `lab13.py` từ `src/` bằng Python trong môi trường tạm có pandas: chương trình kết thúc thành công, 3 phép thử A1 in ĐẠT; D1/E1 vẫn in trạng thái chưa làm.
- Dùng Python đọc kết quả `chay_A()`/`chay_B()`, đối chiếu các bảng A2–A4 và B1–B4 với `bang_chi_phi.md`: khớp các số làm tròn; B2 đúng 3 yếu tố đứng đầu.
- Đọc lại CSV bằng thư viện chuẩn `csv`, tính độc lập chi phí làm lại gấp đôi, cả 3 giới hạn chạy, 2 kịch bản B4, ngưỡng hòa vốn và phân bổ cố định A4: khớp kết quả hàm.
- Dùng số chưa làm tròn để kiểm chứng; giữ kết quả B4 là 12.415 đ [simulated] thay vì chép 12.414 đ từ hướng dẫn, vì phép chia thực tế cho kết quả khoảng 12.414,79 đ [simulated].
- Kiểm tra section E2 có 4 dòng đủ 5 cột, nhãn simulated, link nguồn và nội dung bàn giao; số E2 khớp A/B. Đối chiếu với bản HEAD xác nhận nội dung CP2 và phần E1/event được giữ nguyên.
- `git diff --check`: ĐẠT; `git diff --stat`: chỉ 2 file là `chi_so.md` và báo cáo cá nhân này. Code, CSV, starter, bảng A/B và phần C/D/E3 không đổi.

**Bàn giao:** M3 cần chốt phạm vi, khối lượng theo rollout, an toàn và luật dừng; M4 cần event đo phút/tỉ lệ thực tế, rồi đưa 4 rủi ro vào mục 7 E3 với trạng thái Giả lập. Dữ liệu hiện có đủ để hoàn thành E2, không có phép tính E2 bị chặn bởi D/E1.


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
- Với E2: đọc lại Markdown, kiểm tra dependency, tổng hợp 4 rủi ro từ số A/B, ghi công thức và phân biệt ngưỡng đề xuất với số quan sát.
- Chạy lại chương trình và các phép tính độc lập từ CSV để kiểm chứng E2; chỉ cập nhật section E2 và báo cáo cá nhân này.

**Kiểm soát kết quả AI:**

Tôi giới hạn phạm vi chỉnh sửa của AI trong hai file được phân công, yêu cầu giữ nguyên contract của M1 và không thay đổi dữ liệu gốc. Tôi sử dụng kết quả chạy chương trình, phép tính đối chiếu và báo cáo kiểm tra của Codex để đánh giá tính chính xác của kết quả.

## 6. Tự đánh giá

Tôi đã hoàn thành CP2, bao gồm toàn bộ nhiệm vụ B1–B4, với kết quả đáp ứng ngưỡng sai số theo yêu cầu.

Qua bài lab, tôi hiểu rõ hơn sự khác biệt giữa chi phí sử dụng mô hình AI, chi phí mỗi việc thành công và tổng chi phí vận hành hệ thống.

Kết quả phân tích cho thấy tối ưu giá token không phải yếu tố quan trọng nhất. Giảm lỗi, thời gian xem lại và chi phí làm lại có thể mang lại hiệu quả kinh tế lớn hơn.

Tôi cũng cải thiện kỹ năng phối hợp nhóm, sử dụng contract chung, phân tích độ nhạy và sử dụng công cụ AI trong quy trình phát triển phần mềm.

Điểm cần cải thiện là tăng khả năng kiểm chứng độc lập kết quả do AI tạo ra và nâng cao kỹ năng đánh giá rủi ro kinh tế trước khi triển khai Pilot.

Tôi đã hoàn thành E2 với 4 rủi ro, có nguồn số liệu, công thức, nhãn simulated, tín hiệu theo dõi và vai trò xử lý; kết quả nhất quán với CP1/CP2. Nội dung CP2 đã hoàn thành được giữ nguyên.

Qua E2, tôi nhận ra kết luận kinh tế phải ghi rõ phạm vi, mẫu số, chi phí cố định và phần chuyển nhân viên; ví dụ CPS thấp nhất ở 1 lần chạy không đồng nghĩa tổng chi phí hệ thống thấp nhất.

Giới hạn còn lại: ngưỡng 7%/50%/15% là đề xuất theo tài liệu, chưa được kiểm chứng bằng pilot có đối chứng; phút `_simulated` cần được thay bằng phút đo thật trước khi kết luận vận hành. Tôi cần tiếp tục rèn cách đặt ngưỡng dựa trên dữ liệu thực tế.

Phần việc chuyên môn M2 (CP2 và E2) đã hoàn thành; còn phối hợp bàn giao, giải thích công thức và đối chiếu bản E3 do M4 tổng hợp. Không ghi nhận đã triển khai hoặc kiểm thử phần D, E1, E3 của thành viên khác.
