def tinh_tong_chu_so(n):
    # Đưa về số dương để xử lý
    n = abs(n)
    # Điều kiện dừng: nếu n chỉ còn 1 chữ số
    if n < 10:
        return n
    # Đệ quy: lấy chữ số cuối cùng + gọi lại hàm với phần còn lại
    return (n % 10) + tinh_tong_chu_so(n // 10)

# Chạy thử
n = int(input("Nhập số nguyên n: "))
print(f"Tổng các chữ số của {n} là: {tinh_tong_chu_so(n)}")