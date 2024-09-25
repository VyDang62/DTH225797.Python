
n = 0
while(True):
    n = int(input("Nhap so [0;99]:"))
    if(n < 0 or n > 99):
        continue
    else:
        break

donvi = ["Khong","Mot","Hai","Ba","Bon","Nam","Sau","Bay","Tam","Chin"]
donvichuc = ["","mot","hai","ba","bon","lam","sau","bay","tam","chin"]
chuc = ["","","Hai","Ba","Bon","Nam","Sau","Bay","Tam","Chin"]
if n < 10:
    print("n=",n," => ",donvi[n])
elif n >= 10 and n <= 19:
    c = n // 10
    d = n % 10
    print("n=", n, "=> Muoi", donvichuc[d])
else:
    c = n // 10
    d = n % 10
    print("n=",n,"=>",chuc[c],"muoi",donvichuc[d])
