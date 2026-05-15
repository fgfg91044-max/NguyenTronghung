s = input("Nhap cipher text: ")

ket_qua = ""
i = 0

while i < len(s):
    if s[i] == "#":
        so_lan = int(s[i + 1])
        ky_tu = s[i + 2]

        ket_qua += ky_tu * so_lan

        i += 3
    else:
        ket_qua += s[i]
        i += 1

print("Plain text:", ket_qua)