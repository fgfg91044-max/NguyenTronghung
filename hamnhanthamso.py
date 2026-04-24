def fibonacci(n):
    # Theo định nghĩa trong ảnh: F0 = 1, F1 = 1
    if n == 0 or n == 1:
        return 1
    # Công thức truy hồi: Fn = Fn-1 + Fn-2 nếu n >= 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# --- Chương trình chính để kiểm tra ---
try:
    n = int(input("Nhập số nguyên dương n: "))
    if n < 0:
        print("Vui lòng nhập n >= 0")
    else:
        ket_qua = fibonacci(n)
        print(f"Số hạng thứ {n} của chuỗi Fibonacci là: {ket_qua}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")