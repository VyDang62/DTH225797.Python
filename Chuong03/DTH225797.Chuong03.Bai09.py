while(True):
    m = int(input("Nhap thang: "))
    if m < 0 or m > 12:
        continue
    else:
        break

if m in (1,2,3):
    print("Thang",m,"thuoc quy",1)
elif m in (4,5,6):
    print("Thang", m, "thuoc quy", 2)
elif m in (7,8,9):
    print("Thang", m, "thuoc quy", 3)
elif m in (10,11,12):
    print("Thang", m, "thuoc quy", 4)