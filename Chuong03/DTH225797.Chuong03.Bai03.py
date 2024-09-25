from math import *
a = int(input("Nhap tham so a:"))
b = int(input("Nhap tham so b:"))
c = int(input("Nhap tham so c:"))
delta = (b**2)-4*a*c
if(delta < 0):
    print("Phuong trinh vo nghiem!")
elif (delta ==0):
    print("Phuong trinh co nghiem kep x1 = x2 = ",-b/2*a)
else:
    print("Phuong trinh co 2 nghiem x1 = ",(-b+sqrt(delta))/2*a,", x2 = ",(-b-sqrt(delta))/2*a)