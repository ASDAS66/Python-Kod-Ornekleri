print("*_-*_-*_-*_-*_-*_-*_-*STEAM STORE YE HOŞGELDİNİZ*_-*_-*_-*_-*_-*_-*_-*\n\n\n")
oyun=input("Hangi STEAM oyununu istiyorsunuz?..")
if oyun==("CS GO"):
    version=int(input("Hangi versiyonu istiyorsunuz?."))
    if(version==1 or version==2):
        print("CS:GO ",version,"versiyonun ücreti 30 tl dir.")
    elif (version==3):
        print("CS:GO ",version,"versiyonunun ücreti 40 tl dir.")
    else:
        print("Aradığınız versiyon maalesef mağazamızda bulunmamaktadır.")
elif oyun==("Garrys Mod"):
    print("Garrys Mod oyunun ücreti 15 tl dir.")
elif oyun==("Euro Truck"):
    version=int(input("Hangi versiyonu istiyorsunuz?"))
    if(version==1 or version==2):
        print("Euro Truck ",version," versiyonunun ücreti 20 tl dir.")
    else:
        print("aradığınız versiyon maalesef mağazamızda bulunmaktadır.")
else:
 print("Üzgünüm magazamızda sadece CS:GO, Garrys Mod veya Euro Truck oyunları mevcuttur.")