# f) Tính chu vi hình chữ nhật với chiều dài d và chiều rộng r
rect_perimeter = lambda d, r: (d + r) * 2

# Chạy thử
d = float(input("Nhập chiều dài: "))
r = float(input("Nhập chiều rộng: "))
print(f"Chu vi hình chữ nhật là: {rect_perimeter(d, r)}")