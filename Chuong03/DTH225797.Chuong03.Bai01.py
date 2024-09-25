
y = int(input("Nhap vao nam can kiem tra: "))
if (y % 4 ==0 and y % 100 !=0) or y % 400 ==0:
    print("Nam ",y," la nam nhuan")
else:
    print("Nam ",y," khong la nam nhuan")

