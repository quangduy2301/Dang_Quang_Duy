import random, string, secrets
# Bài 1
print("BÀI 1")
so_xuc_xac = random.randint(1,6)
print("Bạn đã giao ra mặt:",so_xuc_xac)
print()

# Bài 2
print("BÀI 2")
ten = input("Nhập tên: ")
ky_tu_duoc_chon = random.choice(ten)
print("Ký tự may mắn của bạn là:",ky_tu_duoc_chon)
print()

# Bài 3
print("BÀI 3")
tinh_tu = ["Cool","Fast","Smart","Happy"]
danh_tu = ["Tiger","Elephant","Mouse","Hamster"]
One = random.choice(tinh_tu)
Two = random.choice(danh_tu)
print("Tên người dùng gợi ý cho bạn:",One+Two)
print()

# Bài 4
print("BÀI 4")
def tao_ma_pin():
    pin = ""
    for _ in range(4):
        pin += str(random.randint(0, 9))
    return pin

if __name__ == "__main__":
    ma_pin_ngau_nhien = tao_ma_pin()
    print(f"Mã PIN ngẫu nhiên của bạn là: {ma_pin_ngau_nhien}")
print()
    
# Bài 5
print("BÀI 5")
n = int(input("Độ dài mật khẩu: "))
Char = "abcdefghijklmnopqrstuvwxyz"
Passwd_char = ""
for i in range(n):
    Passwd_char += random.choice(Char)
print("Mật khẩu của bạn: ",Passwd_char)
print()

# Bài 6
print("BÀI 6")
s = input("Nhập vào một câu bất kỳ: ")
words = s.split()
random.shuffle(words)
shuffled_sentence = " ".join(words)
print("Câu sau khi xáo trộn:", shuffled_sentence)
print()

# Bài 7
print("BÀI 7")
def tao_mat_khau(n):
  kho_ky_tu = (
      string.ascii_lowercase + string.ascii_uppercase + string.digits + '!@#$%^&*'
  )
  if n < 4:
    return 'Vui lòng nhập độ dài N lớn hơn hoặc bằng 4!'

  mat_khau = [
      random.choice(string.ascii_lowercase),
      random.choice(string.ascii_uppercase),
      random.choice(string.digits),
      random.choice('!@#$%^&*'),
  ]

  for _ in range(n - 4):
    mat_khau.append(random.choice(kho_ky_tu))
    random.shuffle(mat_khau)
    return ''.join(mat_khau)

try:
    N = int(input('Nhập độ dài mật khẩu N: '))
    print('Mật khẩu ngẫu nhiên của bạn:', tao_mat_khau(N))
except ValueError:
    print('Vui lòng nhập một số nguyên hợp lệ.')
print()

# Bài 8
print("BÀI 8")
def tao_mat_khau_ngau_nhien():
    while True:
        try:
            n = int(input("Nhập độ dài mật khẩu mong muốn (N): "))
            if n < 4:
                print("Độ dài mật khẩu nên từ 4 ký tự trở lên để đảm bảo an toàn. Vui lòng thử lại.")
                continue
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")
    chu_cai = string.ascii_letters
    chu_so = string.digits
    ky_tu_dac_biet = string.punctuation
    
    tat_ca_ky_tu = chu_cai + chu_so + ky_tu_dac_biet

    phuong_an_mat_khau = set()
    while len(phuong_an_mat_khau) < 3:
        mat_khau = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(chu_so),
            secrets.choice(ky_tu_dac_biet)
        ]
        mat_khau += [secrets.choice(tat_ca_ky_tu) for _ in range(n - 4)]
        secrets.SystemRandom().shuffle(mat_khau)
        chuoi_mat_khau = "".join(mat_khau)
        phuong_an_mat_khau.add(chuoi_mat_khau)

    print(f"\n--- 3 PHƯƠNG ÁN MẬT KHẨU NGẪU NHIÊN (Độ dài {n}) ---")
    for i, mk in enumerate(phuong_an_mat_khau, 1):
        print(f"Phương án {i}: {mk}")

if __name__ == "__main__":
    tao_mat_khau_ngau_nhien()