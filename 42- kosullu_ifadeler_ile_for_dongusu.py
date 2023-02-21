kullanici_adi=input("kulanıcı adı giriniz : ")
if kullanici_adi=="admin":
    bitis=int(input("kaç kere doneyim. "))
    baslangic=int(input("kactan baslayayım : "))
    artis=int(input("kacar kacar artsın. "))
    for sayi in range (baslangic,bitis, artis):
        print(sayi)
elif kullanici_adi=="uye":
    bitis=int(input("kaç kere döneyim. "))
    for sayi in range (1,bitis,1):
        print(sayi)
else:
    print("admin ya da üye girişi yapınız. ")