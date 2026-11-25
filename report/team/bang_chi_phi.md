# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT (= 1/p, vì 1 − (1 − p)^k triệt tiêu) |

`cd src && python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`.

## A2 · Mô hình chi phí từ trace

Tử số tính mọi lần chạy (1.624 lần, kể cả lần lỗi); mẫu số chỉ đếm yêu cầu có `ket_qua = thanh_cong`. Số lấy từ `mo_hinh(runs, reqs)` với tham số mặc định.

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi × 15 đ) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần**: 4.472 đ [simulated] so với 274,7 đ. So với nhân viên tự làm phải cộng 222 ca không thành công × 12.000 đ: (4.373.585 + 2.664.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated].
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại, 51,8%** [simulated], tiếp theo là xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5% tổng chi phí [simulated], token + tool chỉ 7,5%.

## A3 · Tách theo loại yêu cầu

Mỗi dòng là `mo_hinh(runs, reqs[reqs.loai == loai])`; số lần chạy mỗi yêu cầu = số dòng trong `logix_runs.csv` ÷ số yêu cầu của loại.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× [simulated] |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× [simulated] |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× [simulated] |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× [simulated] |

Tỉ lệ lần chạy có `status = ok` theo lần thử (đo từ trace; số lần chạy trong ngoặc):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% (824) | 75,7% (74) | 38,9% (18) |
| hang_nang | 70,9% (158) | 39,1% (46) | 17,9% (28) |
| quoc_te | 30,0% (150) | 11,4% (105) | 2,2% (93) |
| doi_tac | 51,5% (68) | 18,2% (33) | 14,8% (27) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **quoc_te**: 22.515 đ = 1,88× của 12.000 đ [simulated], chỉ 27,3% thành công dù chạy 2,32 lần/yêu cầu. Chạy lại không giúp: tỉ lệ ok giảm 30,0% → 11,4% → 2,2% vì lỗi lặp lại trên cùng yêu cầu, chạy thêm chỉ tốn tiền. doi_tac sát ngưỡng: 0,85× [simulated], 54,4% thành công.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi có 982 yêu cầu, 900 việc thành công, tổng 3.072.513 đ → chi phí mỗi việc thành công 3.414 đ [simulated]. Việc thành công mỗi tháng = khối lượng × 900 ÷ 1.200 (tỉ lệ trên toàn mẫu, vì 45.000 là tổng yêu cầu mỗi tháng); cố định mỗi việc = 40.000.000 đ ÷ số việc thành công mỗi tháng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× [simulated] |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× [simulated] |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi ở 45.000 yêu cầu/tháng: cộng 1.185 đ/việc, còn **4.599 đ = 0,38×** [simulated]. Khi khối lượng giảm một nửa (ví dụ giai đoạn pilot), cố định tăng gấp đôi lên 2.370 đ/việc → **5.784 đ = 0,48×** [simulated]: vẫn dưới 12.000 đ nhưng nhạy với khối lượng nhỏ, nên mọi con số phải ghi đã cộng cố định hay chưa.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | ... | ... | ... | ... |
| 2 lần | ... | ... | ... | ... |
| 3 lần | ... | ... | ... | ... |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? ...

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: ...
- Kết quả này nói gì về thứ pilot cần học được? ...
