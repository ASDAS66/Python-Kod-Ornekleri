print("1)Kemal Sunal, 2)Fatma Girik, 3)Sezercik, 4)Tarık Akan")
print()
sayi=int(input("karakterlerden birini sec : "))
if sayi>=1 and sayi<=5:
    sayac=0
    for say in range(sayi+1):
        if sayi<=3:
            sayac+=2
            print(sayac*"*", end="")
        elif sayi>3 and sayi<7:
            sayac+=1
            print(sayac*"*", end="")
        elif sayi>=7:
            print("*", end="")
    print(" yıldız gücünde bir karakter seçtin.")
else:
 print("lütfen karakterlerden bir tanesinin numarasını giriniz.")