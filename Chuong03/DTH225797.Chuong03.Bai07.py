d = 0
m = 0
y = 0
while(True):
    d = int(input("Nhap ngay:"))
    if d < 1 or d > 31:
        continue
    m = int(input("Nhap thang:"))
    if m < 1 or m > 12:
        continue
    if m in (4,6,9,11) and d == 31:
        continue
    if m == 2 and d > 29:
        continue
    y = int(input("Nhap nam:"))
    if((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)==False:
        if d == 29:
            continue
        else: break
    else: break

if m in (1,3,5,7,8,10):
    if d == 31:
        print("Ngay tiep theo cua",d,"/",m,"/",y," la",1,"/",m+1,"/",y)
    else:
        print("Ngay tiep theo cua",d,"/",m,"/",y," la",d+1,"/",m,"/",y)
elif m == 12:
    if d == 31:
        print("Ngay tiep theo cua", d, "/", m, "/", y, " la", 1, "/", 1, "/", y+1)
    else:
        print("Ngay tiep theo cua", d, "/", m, "/", y, " la", d+1, "/", m, "/", y)
elif m == 2:
    if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)==True and d == 29:
        print("Ngay tiep theo cua", d, "/", m, "/", y, " la", 1, "/", m + 1, "/", y)
    elif ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)==False and d == 28:
        print("Ngay tiep theo cua", d, "/", m, "/", y, " la", 1, "/", m + 1, "/", y)
    else:
        print("Ngay tiep theo cua", d, "/", m, "/", y, " la", d+1, "/", m, "/", y)
elif m in (4,6,9,11):
    if d == 30:
        print("Ngay tiep theo cua", d, "/", m, "/", y, " la", 1, "/", m + 1, "/", y)
    else:
        print("Ngay tiep theo cua", d, "/", m, "/", y, " la", d+1, "/", m, "/", y)