m = int(input("Nhap thang can tim: "))
if m in (1,3,5,7,8,10,12):
    print("Thang ",m," co 31 ngay!")
elif m in (4,6,9,11):
    print("Thang ",m," co 30 ngay!")
elif m ==2:
    y = int(input("Nhap nam: "))
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("Thang ",m," co 29 ngay!")
    else:
        print("Thang ",m," co 28 ngay!")
else:
    print("Thang ",m," khong hop le!")