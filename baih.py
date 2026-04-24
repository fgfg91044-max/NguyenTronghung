import math

# h) Kiểm tra số nguyên tố
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# Chạy thử
n = int(input("Nhập số nguyên n: "))
if is_prime(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải số nguyên tố.")