# Bài 1
print("BÀI 1")
ten = input("Nhập tên: ")
nam_sinh = int(input("Nhập năm sinh: "))
tuoi = 2026 - nam_sinh
print(f"Xin chào {ten}, năm nay bạn {tuoi} tuổi.")
print()

# Bài 2
print("BÀI 2")
tu_1st = input("Nhập từ thứ nhất: ")
tu_2nd = input("Nhập từ thứ hai: ")
tu_3rd = input("Nhập từ thứ ba: ")
print(tu_1st, tu_2nd, tu_3rd, sep="-")
print("Bạn cùng lớp của chúng mình", end="!!!")
print()
print()

# Bài 3
print("BÀI 3")
ho_ten = input("Nhập họ và tên: ")
print("Tên sau khi chỉnh sửa đúng dạng:",ho_ten.strip().title(),end=".")
print()
print()

# Bài 4
print("BÀI 4")
chuoi = input("Nhập chuỗi: ")
ky_tu = len(chuoi)
print("Tổng số ký tự:",ky_tu)
print("Viết hoa:", chuoi.upper())
print()

# Bài 5
print("BÀI 5")
Str = input("Nhập chuỗi: ")
Str_slicing = Str[::-1]
print(Str_slicing)
if Str == Str_slicing:
    print("Kết quả:",Str_slicing,"LÀ chuỗi đối xứng.")
else:
    print("Kết quả:",Str_slicing,"KHÔNG PHẢI chuỗi đối xứng.")
print()

# Bài 6
print("BÀI 6")
product_id = input("Nhập mã định danh sản phẩm: ")
try:
    parts = product_id.split('-')
    if len(parts) == 3:
        ma_loai = parts[0]
        nam_sx = parts[1]
        ten_loai = parts[2]
        print("\n--- Kết quả tách mã ---")
        print(f"Mã loại sản phẩm: {ma_loai}.")
        print(f"Năm sản xuất: {nam_sx}.")
        print(f"Tên loại sản phẩm: {ten_loai}.")
    else:
        print("Lỗi: Mã định danh không đúng định dạng chuẩn (thừa hoặc thiếu dấu '-').")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}.")
print()

# Bài 7
print("BÀI 7")
full_name = input("Nhập vào họ và tên đầy đủ của nhân viên: ")
parts = full_name.split()

if len(parts) >= 2:
    first_name = parts[-1]
    last_and_middle_name = "".join(parts[:-1])
    email = f"{first_name}.{last_and_middle_name}@company.com".lower()
    print("Địa chỉ email công ty:", email,end=".")
    print()
else:
    print("Vui lòng nhập đầy đủ cả họ và tên.")
print()

# Bài 8
print("BÀI 8")
tieu_de = input("Nhập tiêu đề: ")
print("="*20)
print("*"*3,tieu_de.center(15),"*"*3)
print("="*20)
print()

# Bài 9
print("BÀI 9")
chuoi_nhap = input("Nhập vào một chuỗi: ")
chuoi_lam_sach = chuoi_nhap.strip().lower()
do_dai = len(chuoi_lam_sach)

print("\n--- KẾT QUẢ XỬ LÝ ---")
print(f"Chuỗi sau khi làm sạch: '{chuoi_lam_sach}'.")
print(f"Độ dài thực tế sau khi làm sạch: {do_dai}.")

if do_dai >= 3:
    ba_ky_tu_dau = chuoi_lam_sach[:3]
    ba_ky_tu_cuoi = chuoi_lam_sach[-3:]
    print(f"3 ký tự đầu tiên: '{ba_ky_tu_dau}'.")
    print(f"3 ký tự cuối cùng: '{ba_ky_tu_cuoi}'.")
else:
    print("Chuỗi sau khi làm sạch quá ngắn (dưới 3 ký tự) để lấy đủ 3 ký tự đầu và cuối.")
print()

# Bài 10
print("BÀI 10")
def chuan_hoa(text):
    # Xóa khoảng trắng thừa ở hai đầu và giữa các từ, sau đó viết hoa chữ cái đầu mỗi từ
    cac_tu = text.strip().split()
    text_chuan_hoa = " ".join(cac_tu)
    return text_chuan_hoa.title()

def tao_may_biet_danh():
    print("=" * 40)
    print("      MÁY TẠO BIỆT DANH SIÊU HÙNG      ")
    print("=" * 40)
    ten_that = input("Nhập tên thật của bạn: ")
    mau_yeu_thich = input("Nhập màu sắc yêu thích: ")
    con_vat_yeu_thich = input("Nhập con vật yêu thích: ")
    ten_chuan = chuan_hoa(ten_that)
    mau_chuan = chuan_hoa(mau_yeu_thich)
    vat_chuan = chuan_hoa(con_vat_yeu_thich)
    ten_khong_dau_cach = "".join(ten_chuan.split())
    ba_ky_tu_cuoi = ten_khong_dau_cach[-3:] if len(ten_khong_dau_cach) >= 3 else ten_khong_dau_cach
    ky_tu_dao_nguoc = ba_ky_tu_cuoi[::-1].title()
    
    biet_danh = f"{mau_chuan} {vat_chuan} {ky_tu_dao_nguoc}"
    lines = [
        "THẺ THÔNG TIN SIÊU HÙNG",
        "-" * 30,
        f"Họ và tên: {ten_chuan}",
        f"Sức mạnh màu sắc: {mau_chuan}",
        f"Linh thú đồng hành: {vat_chuan}",
        "-" * 30,
        f"BIỆT DANH: {biet_danh.upper()}"
    ]
    
    max_len = max(len(line) for line in lines)
    khung_width = max_len + 4
    
    print("\n" + "*" * khung_width)
    for line in lines:
        if line.startswith("-"):
            print("*" + line.center(khung_width - 2, "-") + "*")
        else:
            print(f"* {line.ljust(khung_width - 4)} *")
    print("*" * khung_width)

if __name__ == "__main__":
    tao_may_biet_danh()