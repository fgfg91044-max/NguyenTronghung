import math

# g) Kiểm tra số chính phương (số có căn bậc hai là số nguyên)
is_perfect_square = lambda n: n >= 0 and math.isqrt(n)**2 == n

# Chạy thử
n = int(input("Nhập số nguyên n: "))
if is_perfect_square(n):
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải số chính phương.")