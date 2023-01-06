#parolanın uzunluguna göre işlem yapan python kodu
parola=input("Parolanizi giriniz : ")
uzunluk=len(parola)
mesaj="Parolanız toplam {} karakterden oluşuyor!" 
if uzunluk > 12:
    print(mesaj.format (uzunluk))
    print(" Parolanızın toplam uzunluğu 12 karakteri geçmemeli!")
else:
    print("sisteme hosgeldiniz....")