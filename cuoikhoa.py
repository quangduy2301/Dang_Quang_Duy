while True:
    print("=======================================")
    print("********QUẢN LÝ TỦ SÁCH CÁ NHÂN********")
    print("=======================================")
    print("[1] Thêm sách mới")
    print("[2] Xem toàn bộ tủ sách")
    print("[3] Tìm kiếm")
    print("[4] Thông kê")
    print("[5] Kết thúc")
    print()
    lua_chon = int(input("Lựa chọn của bạn: "))
    if lua_chon == 1:
        while True:
            ten_sach = input("Nhập tên sách: ").strip().title()
            if ten_sach != "":
                nguoi = input("Nhập tác giả: ").strip().title()
                if nguoi != "":
                    xuat_ban = input("Nhập năm xuất bản: ").strip()
                    so_ky_tu = len(xuat_ban)
                    if xuat_ban.isdigit() and xuat_ban != "" and so_ky_tu == 4:
                        the_loai_sach = input("Nhập thể loại: ").strip()
                        if the_loai_sach != "":
                            trang_thai_sach = input("Trạng thái sách ([1] Đã đọc [2] Chưa đọc): ").strip()
                            if trang_thai_sach != "" and trang_thai_sach.isdigit() and trang_thai_sach == "1":
                                print()
                                print("Thông báo: Thêm sách thành công!")
                                print(f"Tên sách: {ten_sach}\nTác giả: {nguoi}\nNăm xuất bản: {xuat_ban}\nThể loại: {the_loai_sach}\nTrạng thái: Đã đọc")
                                print()
                                break
                            elif trang_thai_sach != "" and trang_thai_sach.isdigit() and trang_thai_sach == "2":
                                print()
                                print("Thông báo: Thêm sách thành công!")
                                print(f"Tên sách: {ten_sach}\nTác giả: {nguoi}\nNăm xuất bản: {xuat_ban}\nThể loại: {the_loai_sach}\nTrạng thái: Chưa đọc")
                                print()
                                break
                            elif (trang_thai_sach != "" and trang_thai_sach.isdigit()) and (not trang_thai_sach == "1" or not trang_thai_sach == "2"):
                                print("Cảnh báo: Bạn cần đúng nhập số cho trạng thái sách.")
                            else:
                                print("Cánh báo: Số cho trạng thái sách không được để trống!")
                        else:
                            print("Cảnh báo: Thể loại sách không được để trống!")
                    elif xuat_ban.isdigit() and xuat_ban != "" and not so_ky_tu == 4:
                        print("Cảnh báo: Năm xuất bản phải là số có 4 chữ số.")
                    else:
                        print("Cảnh báo: Năm xuất bản không được để trống!")
                else:
                    print("Cảnh báo: Tác giả không được để trống!")
            else:
                print("Cảnh báo: Tên sách không được để trống!")
            print()
    elif lua_chon == 2:
        pass
    elif lua_chon == 3:
        pass
    elif lua_chon == 4:
        pass
    elif lua_chon == 5:
        print("Thông báo: Bạn đã kết thúc dự án tủ sách cá nhân của bạn.")
        break
    else:
        print("Cảnh báo: Lựa chọn của bạn không đúng!")