def ucln(a, b):
    # Thuật toán Euclid đệ quy
    # Điều kiện dừng: nếu b bằng 0 thì UCLN là a
    if b == 0:
        return a
    # Đệ quy: UCLN(a, b) = UCLN(b, a % b)
    return ucln(b, a % b)

# Chạy thử
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
print(f"Ước số chung lớn nhất của {a} và {b} là: {ucln(a, b)}")