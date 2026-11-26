sach = []
def hien_thi_sach(thong_tin_sach, so_thu_tu=None):
    if so_thu_tu is not None:
        print(f"\nSách số {so_thu_tu}:")
    print(f"Tên sách: {thong_tin_sach['ten']}")
    print(f"Tác giả: {thong_tin_sach['tac_gia']}")
    print(f"Năm xuất bản: {thong_tin_sach['nam_xuat_ban']}")
    print(f"Thể loại: {thong_tin_sach['the_loai']}")
    print(f"Trạng thái: {thong_tin_sach['trang_thai']}")

def them_sach():
    while True:
        ten_sach = input("Nhập tên sách: ").strip().title()
        if ten_sach:
            break
        print("Cảnh báo: Tên sách không được để trống!")

    while True:
        tac_gia = input("Nhập tác giả: ").strip().title()
        if tac_gia:
            break
        print("Cảnh báo: Tác giả không được để trống!")

    while True:
        nam_xuat_ban = input("Nhập năm xuất bản (4 chữ số): ").strip()
        if nam_xuat_ban.isdigit() and len(nam_xuat_ban) == 4:
            break
        print("Cảnh báo: Năm xuất bản phải gồm đúng 4 chữ số.")

    while True:
        the_loai = input("Nhập thể loại: ").strip().title()
        if the_loai:
            break
        print("Cảnh báo: Thể loại sách không được để trống!")

    while True:
        trang_thai = input(
            "Trạng thái sách ([1] Đã đọc [2] Chưa đọc): "
        ).strip()
        if trang_thai == "1":
            trang_thai = "Đã đọc"
            break
        if trang_thai == "2":
            trang_thai = "Chưa đọc"
            break
        print("Cảnh báo: Chi được chọn 1 hoặc 2.")

    thong_tin_sach = {
        "ten": ten_sach,
        "tac_gia": tac_gia,
        "nam_xuat_ban": nam_xuat_ban,
        "the_loai": the_loai,
        "trang_thai": trang_thai,
    }
    sach.append(thong_tin_sach)
    print("\nThông báo: Thêm sách thành công!")
    hien_thi_sach(thong_tin_sach)
    print()


def xem_tu_sach():
    if not sach:
        print("Thông báo: Không có sách nào trong tủ sách của bạn.\n")
        return

    print(f"\nTủ sách hiện có {len(sach)} cuốn:")
    for so_thu_tu, thong_tin_sach in enumerate(sach, start=1):
        hien_thi_sach(thong_tin_sach, so_thu_tu)
    print()


def tim_kiem_sach():
    tu_khoa = input("Nhập từ khóa (tên sách, tác giả hoặc thể loại): ").strip()
    if not tu_khoa:
        print("Cảnh báo: Từ khóa không được để trống!\n")
        return

    tu_khoa = tu_khoa.casefold()
    ket_qua = [
        thong_tin_sach
        for thong_tin_sach in sach
        if any(
            tu_khoa in thong_tin_sach[truong].casefold()
            for truong in ("ten", "tac_gia", "the_loai")
        )
    ]
    if not ket_qua:
        print("Thông báo: Không tìm thấy sách nào trong tủ sách của bạn.\n")
        return

    print(f"\nTìm thấy {len(ket_qua)} cuốn sách:")
    for so_thu_tu, thong_tin_sach in enumerate(ket_qua, start=1):
        hien_thi_sach(thong_tin_sach, so_thu_tu)
    print()


def thong_ke():
    if not sach:
        print("Thông báo: Không thể thống kê vì tủ sách của bạn đang trống.\n")
        return

    da_doc = sum(1 for thong_tin_sach in sach if thong_tin_sach["trang_thai"] == "Đã đọc")
    chua_doc = len(sach) - da_doc
    sach_theo_the_loai = {}
    for thong_tin_sach in sach:
        the_loai = thong_tin_sach["the_loai"]
        sach_theo_the_loai[the_loai] = sach_theo_the_loai.get(the_loai, 0) + 1

    print("\nThống kê tủ sách của bạn:")
    print(f"Tổng số sách: {len(sach)}")
    print(f"Sách đã đọc: {da_doc}")
    print(f"Sách chưa đọc: {chua_doc}")
    print("Số sách theo thể loại:")
    for the_loai, so_luong in sorted(sach_theo_the_loai.items()):
        print(f"- {the_loai}: {so_luong}")
    print()


def lay_tung_sach():
    if not sach:
        print("Thông báo: Không có sách nào trong tủ sách của bạn.\n")
        return

    tu_khoa = input("Nhập tên sách muốn lấy: ").strip().casefold()
    ket_qua = [
        (vi_tri, thong_tin_sach)
        for vi_tri, thong_tin_sach in enumerate(sach)
        if thong_tin_sach["ten"].casefold() == tu_khoa
    ]
    if not ket_qua:
        print("Cảnh báo: Không có sách nào trùng tên!\n")
        return

    print("\nCác sách trùng tên:")
    for so_thu_tu, (_, thong_tin_sach) in enumerate(ket_qua, start=1):
        hien_thi_sach(thong_tin_sach, so_thu_tu)

    while True:
        lua_chon_sach = input("Chọn số thứ tự sách muốn lấy: ").strip()
        if lua_chon_sach.isdigit() and 1 <= int(lua_chon_sach) <= len(ket_qua):
            vi_tri, thong_tin_sach = ket_qua[int(lua_chon_sach) - 1]
            break
        print("Cảnh báo: Số thứ tự không hợp lệ!")

    while True:
        xac_nhan = input(
            f"Bạn có muốn lấy sách '{thong_tin_sach['ten']}' khỏi tủ sách của bạn không (c/k)? "
        ).strip().casefold()
        if xac_nhan == "c":
            sach.pop(vi_tri)
            print("Thông báo: Đã lấy sách khỏi tủ sách của bạn.\n")
            return
        if xac_nhan == "k":
            print("Thông báo: Sách vẫn được giữ trong tủ sách của bạn.\n")
            return
        print("Cảnh báo: Lựa chọn của bạn không đúng!")

def lay_het_sach():
    if not sach:
        print("Thông báo: Không có sách nào trong tủ sách của bạn.\n")
        return

    while True:
        xac_nhan = input(
            f"Bạn có muốn lấy hết {len(sach)} cuốn sách khỏi tủ sách của bạn không (c/k)? "
        ).strip().casefold()
        if xac_nhan == "c":
            sach.clear()
            print("Thông báo: Đã lấy toàn bộ sách khỏi tủ sách của bạn.\n")
            return
        if xac_nhan == "k":
            print("Thông báo: Sách vẫn được giữ trong tủ sách của bạn.\n")
            return
        print("Cảnh báo: Lựa chọn của bạn không đúng!")

def main():
    while True:
        print("===============================")
        print("********QUẢN LÝ TỦ SÁCH********")
        print("===============================")
        print("[1] Thêm sách mới")
        print("[2] Xem toàn bộ tủ sách")
        print("[3] Tìm kiếm sách")
        print("[4] Thống kê")
        print("[5] Lấy từng sách")
        print("[6] Lấy hết sách")
        print("[7] Kết thúc\n")
        lua_chon = input("Lựa chọn của bạn: ").strip()
        if lua_chon == "1":
            them_sach()
        elif lua_chon == "2":
            xem_tu_sach()
        elif lua_chon == "3":
            tim_kiem_sach()
        elif lua_chon == "4":
            thong_ke()
        elif lua_chon == "5":
            lay_tung_sach()
        elif lua_chon == "6":
            lay_het_sach()
        elif lua_chon == "7":
            print("Thông báo: Bạn đã kết thúc dự án tủ sách của bạn.")
            break
        else:
            print("Cảnh báo: Lựa chọn của bạn không đúng!\n")

if __name__ == "__main__":
    main()
