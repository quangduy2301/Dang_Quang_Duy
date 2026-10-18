from time import *
import random, string
def chuong_trinh_tao_mat_khau():
    # 1. In giao diện chào mừng chương trình ra màn hình Terminal
    print("=========================================")
    print("  CHƯƠNG TRÌNH TỰ ĐỘNG TẠO MẬT KHẨU ")
    print("=========================================")

    # 2. Hỏi người dùng độ dài mật khẩu mong muốn
    sleep(0.5)
    while True:
        try:
            do_dai = int(input("Nhập độ dài mật khẩu mong muốn: "))
            if do_dai > 0:
                break
            print("Vui lòng nhập một số nguyên lớn hơn 0.")
            sleep(0.5)
        except ValueError:
            print("Định dạng không hợp lệ. Vui lòng nhập một số nguyên.")
            sleep(0.5)

    # 3. Hỏi người dùng 3 câu hỏi tùy chọn (nhập y hoặc n)
    sleep(0.5)
    print("\nChọn các thành phần cho mật khẩu (y: Có, n: Không):")

    chon_hoa = input("Có muốn bao gồm chữ HOA (A-Z) không? ").strip().lower()
    chon_so = input("Có muốn bao gồm chữ SỐ (0-9) không? ").strip().lower()
    chon_dac_biet = (
        input("c. Có muốn bao gồm KÝ TỰ ĐẶC BIỆT (!@#$%^&*) không? ")
        .strip()
        .lower()
    )

    # 4. Tự động tổng hợp kho ký tự phù hợp (Mặc định luôn có chữ cái thường a-z)
    kho_ky_tu = string.ascii_lowercase

    if chon_hoa == "y":
        kho_ky_tu += string.ascii_uppercase
    if chon_so == "y":
        kho_ky_tu += string.digits
    if chon_dac_biet == "y":
        kho_ky_tu += "!@#$%^&*"

    # 5. Sử dụng vòng lặp để chọn ngẫu nhiên từng ký tự ghép thành mật khẩu hoàn chỉnh
    mat_khau = ""
    for _ in range(do_dai):
        ky_tu_ngau_nhien = random.choice(kho_ky_tu)
        mat_khau += ky_tu_ngau_nhien

    # 6. In kết quả
    sleep(0.5)
    print("\n-----------------------------------------")
    print(f"Mật khẩu của bạn đã được tạo thành công: {mat_khau}")
    print("-----------------------------------------")


# Chạy chương trình
if __name__ == "__main__":
    chuong_trinh_tao_mat_khau()