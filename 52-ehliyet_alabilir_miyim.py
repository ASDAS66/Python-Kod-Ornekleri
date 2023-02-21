#Adım 1: Başla
# Adım 2: Yaş ve isim bilgilerini iste
# Adım 3: yas > 18 değilse ehliyet alamaz
# Adım 4: yas > 18 ise eğitim bilgilerini iste (İlköğretim, Ortaöğretim, Lise, Lisans, YüksekLisans, Doktora)
# Adım 5: Eğitim, eğer ortaöğretim veya ilk öğretim ise ehliyet alamaz
# Adım 6: Bitir.

isim=input("isminizi giriniz : ")
yas=int(input("yasınızı giriniz : "))

if(yas<18):
    print(f"Merhaba {isim}, yaşın 18 den küçük oldugu için ehliyet alamazsın...")
else:
    egitim=input("lütfen öğrenim durumunuzu giriniz...")
    if (egitim=="ilköğretim "or egitim=="ortaokul"):
        print("maalesef eğitim durumunuz yetersizdir.")
    else:
        print(f"merhaba{isim} ehliyet alabilirsin")