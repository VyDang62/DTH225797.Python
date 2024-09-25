a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
while(True):
    pt = input("Nhap phep toan + - * /:")
    if pt in ('+','-','*','/'):
        break
    else:
        continue

if pt == '+':
    print("Ket qua:",a,pt,b,"=",a+b)
elif pt == '-':
    print("Ket qua:", a, pt, b, "=", a - b)
elif pt == '*':
    print("Ket qua:", a, pt, b, "=", a * b)
else:
    print("Ket qua:", a, pt, b, "=", a / b)