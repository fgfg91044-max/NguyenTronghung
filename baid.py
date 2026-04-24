# d) Kiểm tra n có là bội số của 13 hoặc 19 hay không
is_multiple = lambda n: n % 13 == 0 or n % 19 == 0

# Chạy thử
n = int(input("Nhập số nguyên n: "))
if is_multiple(n):
    print(f"{n} là bội số của 13 hoặc 19.")
else:
    print(f"{n} không phải bội số của 13 hay 19.")