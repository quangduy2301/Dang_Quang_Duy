from time import *
import random, string
# Bài 1
print("BÀI 1")
ho_ten = "Đặng Quang Duy"
tuoi = 17
chieu_cao = 1.82
dang_di_hoc = True
print(f"Tên: {ho_ten}")
print(type(ho_ten))
print(f"Tuổi: {tuoi}")
print(type(tuoi))
print(f"Chiều cao: {chieu_cao}")
print(type(chieu_cao))
print(f"Đang đi học: {dang_di_hoc}")
print(type(dang_di_hoc))
print()

# Bài 2
sleep(0.5)
print("BÀI 2")
print("""
1. CÁC BIẾN SAU HỢP LỆ: ho_ten, diemTB.
2. CÁC BIẾN SAU SAI: 2diem, tong tien, class, so-luong.
3. LÝ DO SAI & CÁCH SỬA
    a. Lý do sai
        - 2diem: Tên biến này sai vì bắt đầu bằng 1 chữ số, trong khi yêu cầu tên biến bắt đầu bằng một chữ cái.
        - tong tien: Tên biến này sai vì có dấu cách, trong khi không được phép cho dấu cách nào.
        - class: Tên biến này sai vì có từ khóa Python, trong khi không được phép cho từ khóa Python nào.
        - so-luong: Tên biến này sai vì chứa ký tự dấu "-", ký tự không được phép sử dụng trong tên biến.
    b. Cách sửa
        - 2diem: Thay thành "diem2".
        - tong tien: Thay thành "tong_tien".
        - class: Thay thành "lop".
        - so-luong: Thay thành "so_luong".
""")

# Bài 3
sleep(0.5)
print("BÀI 3")
a = 17
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print()
so = int(input("Nhập số: "))
if so % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")
print()

# Bài 4
sleep(0.5)
print("BÀI 4")
Letter = "a"
Letter2 = "b"
Letter3 = "c"
Str = "Xin chào"
Str2 = "Tạm biệt"
nam = 2025
thang = 10
ngay = 25
print(Letter, Letter2, Letter3, sep="-")
print(Str, end="!")
print(Str2, end="!")
print()
print(nam, thang, ngay, sep="/")
print()

# Bài 5
sleep(0.5)
print("BÀI 5")
ten = str(input("Nhập tên: "))
tuoi = int(input("Nhập tuổi: "))
print(f"Xin chào {ten}! Sang năm bạn {tuoi} tuổi.")
print()
chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
chu_vi = (chieu_dai + chieu_rong) * 2
dien_tich = chieu_dai * chieu_rong
print(f"Chu vi hình chữ nhật: {chu_vi}")
print(f"Diện tích hình chữ nhật: {dien_tich}")
print()

# Bài 6
sleep(0.5)
print("BÀI 6")
chuoi = "Python"
print(f"Chuỗi: {chuoi}")
print(f"Ký tự đầu: {chuoi[0]}")
print(f"Ký tự cuối: {chuoi[-1]}")
print(f"3 ký tự đầu: {chuoi[:3]}")
print(f"Đảo ngược: {chuoi[::-1]}")
print(chuoi,chuoi,chuoi,sep="-")
print()

# Bài 7
sleep(0.5)
print("BÀI 7")
toan = float(input("Nhập điểm môn Toán: "))
van = float(input("Nhập điểm môn Văn: "))
trung_binh = (toan + van) / 2

# Tiêu chí 1: Cả hai môn trên 5
if toan >= 5 and van >= 5:
    print(f"Cả hai môn trên 5: {True}")
else:
    print(f"Cả hai môn trên 5: {False}")
    
# Tiêu chí 2: Có ít nhất một môn trên 8
if toan >= 8 or van >= 8:
    print(f"Có ít nhất một môn trên 8: {True}")
else:
    print(f"Có ít nhất một môn trên 8: {False}")

# Tiêu chí 3: Có bị điểm liệt
if toan < 3 or van < 3:
    print(f"Bị điểm liệt: {True}")
else:
    print(f"Bị điểm liệt: {False}")
    
# Tiêu chí cuối: Đạt học sinh giỏi
if trung_binh >= 8 and toan >= 6 and van >= 6:
    print(f"Đạt học sinh giỏi: {True}")
else:
    print(f"Đạt học sinh giỏi: {False}")
print()

# Bài 8
sleep(0.5)
ho_va_ten = str(input("Nhập họ và tên: "))
print(f"Họ và tên sau khi bỏ khoảng trắng: {ho_va_ten.strip()}")
print(f"Chữ hoa: {ho_va_ten.upper()}")
print(f"Chữ thường: {ho_va_ten.lower()}")
ky_tu = len(ho_va_ten)
print(f'Họ tên "{ho_va_ten.upper()}" có {ky_tu} ký tự.')
print()

# Bài 9
sleep(0.5)
print("BÀI 9")
Str_ho_ten = str(input("Nhập họ và tên: "))
cac_tu = Str_ho_ten.strip().split()
ho = cac_tu[0]
ten = cac_tu[-1]
so = random.randint(10, 99)
username = (f"Tên đăng nhập của bạn là: {ho[:3].lower()}{ten[::-1].lower()}{so}.")
print(username)
print()

# Bài 10
print("BÀI 10")
import random
import string

chu_thuong = string.ascii_lowercase
chu_hoa = string.ascii_uppercase
chu_so = string.digits
dac_biet = "!@#$%&*"
toan_bo = chu_thuong + chu_hoa + chu_so + dac_biet

do_dai = int(input("Nhập độ dài mật khẩu (ít nhất 8 ký tự): "))

if do_dai >= 8:
  # 1. Lấy ít nhất 1 ký tự từ mỗi nhóm bắt buộc
  mat_khau_list = [
      random.choice(chu_thuong),
      random.choice(chu_hoa),
      random.choice(chu_so),
      random.choice(dac_biet),
  ]

  # 2. Lấy ngẫu nhiên các ký tự còn lại từ kho gộp chung
  so_ky_tu_con_lai = do_dai - len(mat_khau_list)
  for _ in range(so_ky_tu_con_lai):
    mat_khau_list.append(random.choice(toan_bo))

  # 3. Dùng random.shuffle để xáo trộn danh sách
  random.shuffle(mat_khau_list)

  # 4. Dùng "".join() ghép lại thành mật khẩu hoàn chỉnh
  mat_khau = "".join(mat_khau_list)

  print("Mật khẩu ngẫu nhiên của bạn là:", mat_khau)
else:
  print("Thiếu số ký tự tối thiểu.")