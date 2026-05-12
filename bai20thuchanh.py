def tinh_tien_thoi(so_tien):
    # Danh sách các mệnh giá tiền, sắp xếp giảm dần để số lượng tờ là ít nhất
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    print(f"So tien {so_tien} duoc doi thanh:")
    
    tong_so_to = 0
    tong_so_loai = 0
    
    for tien in menh_gia:
        so_to = so_tien // tien # Tính số tờ của mệnh giá hiện tại
        if so_to > 0:
            print(f"Loai {tien} gom {so_to} to")
            tong_so_to += so_to
            tong_so_loai += 1
            so_tien %= tien # Cập nhật lại số tiền còn lại cần đổi
            
    print(f"Tong cong co {tong_so_to} to")
    print(f"Tong so loai = {tong_so_loai}")

def main():
    try:
        a = int(input("Nhập số tiền hàng cần thanh toán (a): "))
        b = int(input("Nhập số tiền khách đưa (b): "))
        
        print("-" * 30)
        if a > b:
            print(f"Số tiền khách hàng còn thiếu là: {a - b}")
        elif a == b:
            print("Cám ơn khách hàng. Hẹn gặp lại")
        else: # a < b
            tien_thoi = b - a
            # Gọi hàm tính tiền thối lại cho khách
            tinh_tien_thoi(tien_thoi)
            
            # Đợi người dùng nhấn Enter
            input("\n(Nhấn Enter để tiếp tục...)")
            print("Cám ơn khách hàng. Hẹn gặp lại")
            
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

if __name__ == "__main__":
    main()