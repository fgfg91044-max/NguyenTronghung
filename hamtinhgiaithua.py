def giai_thua(n):
    # Điều kiện dừng: 0! = 1 và 1! = 1
    if n == 0 or n == 1:
        return 1
    # Đệ quy: n! = n * (n-1)!
    return n * giai_thua(n - 1)

# Chạy thử
n = int(input("Nhập số nguyên dương n: "))
if n < 0:
    print("Vui lòng nhập số dương.")
else:
    print(f"{n}! = {giai_thua(n)}")