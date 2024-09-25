try:
    toan = float(input("Nhap diem toan:"))
    ly = float(input("Nhap diem ly:"))
    hoa = float(input("Nhap diem hoa:"))
except:
    print("Loi!")

dtb = (toan+ly+hoa)/3
print("Diem trung binh:",dtb)
print("Diem trung binh lam tron:",round(dtb,2))

