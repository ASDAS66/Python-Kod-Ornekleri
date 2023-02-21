#yağmur hastaney gider ve hastane kayıt masasındaki cihaz 1,4 ve 7.
#ve 10. parmağı için parmak izi almakzorunda oldugunu söyler.
#toplamda 4 kez parmak izi alacak python kodunu yazınız.
print("*******HASTANEMİZE HOŞ GELDİNİZ********")
for sayi in range(1,11,3):
    print(sayi,". parmagınızı okutunuz.")
print("********SAĞLIKLI GÜNLER DİLERİZ********")

#10 A KADAR YAZILDIGI HALDE 2. VE 10. PARMAGI ALMASIN İSTERSEK
for sayi in range(1,10,2):
    if sayi==6 or sayi==10:
        break
