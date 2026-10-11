# Bài 1
print("BÀI 1")
name = input("Nhập tên học sinh: ")
age = int(input("Nhập tuổi: "))
height = float(input("Nhập chiều cao: "))
is_student = True
print("Tên học sinh:", name)
print("Tuổi:", age)
print("Chiều cao", height)
if is_student:
    print("Có phải học sinh")
else:
    print("Không phải học sinh")
print()
    
# Bài 2
print("BÀI 2")
a = 15
b = 3.14
c = "Python"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()

# Bài 3
print("BÀI 3")
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
print("Tổng:", a+b)
print("Hiệu:", a-b)
print("Tích:", a*b)
print("Thương:", a/b)
print()

# Bài 4
print("BÀI 4")
chieu_dai = float(input("Nhập chiều dài (cm): "))
chieu_rong = float(input("Nhập chiều rộng (cm): "))
print("Chu vi hình chữ nhật:", (chieu_dai+chieu_rong)*2, "cm")
print("Diện tích hình chữ nhật:", chieu_dai*chieu_rong, "cm2")
print()

# Bài 5
print("BÀI 5")
toan = float(input("Điểm môn Toán: "))
van = float(input("Điểm môn Văn: "))
anh = float(input("Điểm môn Anh: "))
diem_trung_binh = round((toan+van+anh)/3,2)
print("Toán:", toan)
print("Văn:", van)
print("Anh:", anh)
print("Điểm trung bình:", diem_trung_binh)
print()

# Bài 6
phut = int(input("Nhập số phút: "))
gio = phut // 60
phut = phut % 60
print("Kết quả:", gio, "giờ", phut, "phút")
print()

# Bài 7
print("BÀI 7")
n = int(input("Nhập số nguyên có 3 chữ số: "))
tram = n // 100
chuc = (n // 10) % 10
donvi = n % 10
print("Hàng trăm:", tram)
print("Hàng chục:", chuc)
print("Hàng đơn vị:", donvi)
print()

# Bài 8
print("BÀI 8")
a = int(input("Số thứ nhất: "))
b = int(input("Số thứ hai: "))
luy_thua = a**n
print("Lũy thừa:", luy_thua)
print()

# Bài 9
print("BÀI 9")
C = float(input("Nhập nhiệt độ (độ C): "))
F = round(C * 9 / 5 + 32, 1)
print("Nhiệt độ được chuyển đổi sang độ F là:", F)
print()

# Bài 10
print("BÀI 10")
ten_san_pham = input("Nhập tên sản phẩm: ")
don_gia = 2000
so_luong = int(input("Bạn mua bao nhiêu cái? "))
thanh_tien = don_gia * so_luong
print("Bạn mua", so_luong, ten_san_pham + ",", "tổng tiền là", thanh_tien, "đồng.")
print()

# Bài 11
print("BÀI 11")
n = int(input("Nhập số: "))
if n > 0:
    print(True)
else:
    print(False)
print()

# Bài 12
print("BÀI 12")
tuoi = int(input("Nhập tuổi: "))
if tuoi >= 6 and tuoi <= 18:
    print("Có nằm trong độ tuổi 6 - 18")
else:
    print("Không nằm trong độ tuổi 6 - 18")
print()

# Bài 13
print("BÀI 13")
x = int(input("Nhập số: "))
if x >= 10 and x <= 50:
    print("Có nằm trong khoảng")
else:
    print("Không nằm trong khoảng")
print()

# Bài 14
print("BÀI 14")
age = int(input("Nhập tuổi: "))
has_ticket = True
if age >= 10 and has_ticket:
    print("Có vé và đủ 10 tuổi trở lên. Có được tham gia trò chơi.")
else:
    print("Không có vé hoặc chưa đủ 10 tuổi. Không được tham gia trò chơi.")
print()

# Bài 15
print("BÀI 15")
n = int(input("Nhập số: "))
if n % 2 == 0:
    print("Có phải số chẵn")
else:
    print("Không phải số chẵn")
print()

# Bài 16
print("BÀI 16")
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
print("a + b =",a+b)
print("a - b =",a-b)
print("a * b =",a*b)
print("a / b =",a/b)
print("a // b =",a//b)
print("a % b =",a%b)
print("a ** b =",a**b)
print()

# Bài 17
print("BÀI 17")
ten_san_pham = input("Nhập tên sản phẩm: ")
don_gia = int(input("Nhập đơn giá: "))
so_luong = int(input("Số lượng: "))
thanh_tien = don_gia * so_luong
phan_tram_giam = float(input("Phần trăm giảm: "))
tien_giam = thanh_tien * phan_tram_giam / 100
phai_tra = thanh_tien - tien_giam
print()
print("HÓA ĐƠN")
print("Tên sản phẩm:", ten_san_pham)
print("Đơn giá:", don_gia)
print("Số lượng:", so_luong)
print("Thành tiền:", thanh_tien)
print("Phần trăm giảm:", phan_tram_giam)
print("Phải trả:", phai_tra)
print()

# Bài 18
print("BÀI 18")
toan = float(input("Điểm môn Toán: "))
van = float(input("Điểm môn Văn: "))
anh = float(input("Điểm môn Anh: "))
diem_trung_binh = (toan+van+anh)/3
if (toan < 6.5 or van < 6.5 or anh < 6.5) and diem_trung_binh < 8:
    print("Đạt điều kiện học bổng:", False)
else:
    print("Đạt điều kiện học bổng:", True)
print()
    
# Bài 19
print("BÀI 19")
nam_sinh = int(input("Nhập năm sinh: "))
hien_tai = int(input("Nhập năm hiện tại: "))
tuoi = hien_tai - nam_sinh
if tuoi >= 13:
    print("Từ 13 tuổi:", True)
else:
    print("Từ 13 tuổi", False)
if tuoi >= 13 and tuoi <= 18:
    print("Từ 13 - 18 tuổi:", True)
else:
    print("Từ 13 - 18 tuổi:", False)
if tuoi < 18:
    print("Dưới 18 tuổi:", True)
else:
    print("Dưới 18 tuổi:", False)
print()