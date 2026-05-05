import math

# Namespace/Identity: Nguyễn_Trọng_Hùng_2411110034

def is_prime(n):
    """Hàm kiểm tra số nguyên tố"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    numbers = []

    # Vòng lặp cho phép người dùng nhập nhiều lần
    while True:
        try:
            num = int(input("Nhập một số nguyên: "))
            numbers.append(num)
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
            continue

        choice = input("Bạn có muốn nhập nữa không? (Yes/No hoặc Y/N): ").strip().lower()
        if choice in ['no', 'n']:
            break

    # Kiểm tra nếu danh sách trống
    if not numbers:
        print("Danh sách trống. Chương trình kết thúc.")
        return

    print("\n--- KẾT QUẢ ---")
    print(f"Danh sách bạn vừa nhập: {numbers}\n")

    # a) In ra các số nguyên tố có trong list
    primes = [n for n in numbers if is_prime(n)]
    print(f"a) Các số nguyên tố có trong list là: {primes}")

    # b) Tính trung bình cộng các số âm, trung bình các số dương
    positives = [n for n in numbers if n > 0]
    negatives = [n for n in numbers if n < 0]

    avg_pos = sum(positives) / len(positives) if positives else 0
    avg_neg = sum(negatives) / len(negatives) if negatives else 0

    print(f"b) Trung bình cộng các số dương: {avg_pos}")
    print(f"   Trung bình cộng các số âm: {avg_neg}")

    # c) Số lớn nhất, số nhỏ nhất
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"c) Số lớn nhất: {max_num}")
    print(f"   Số nhỏ nhất: {min_num}")

    # d) Cho biết các số trong list có được sắp xếp tăng dần hay chưa?
    # So sánh list hiện tại với phiên bản đã được sắp xếp của chính nó
    is_sorted = numbers == sorted(numbers)
    if is_sorted:
        print("d) Các số trong list ĐÃ được sắp xếp tăng dần.")
    else:
        print("d) Các số trong list CHƯA được sắp xếp tăng dần.")

if __name__ == "__main__":
    main()