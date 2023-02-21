tekrar=int(input("şimdi bir oyun oynayalım. Kaç kere oynamak istiyorsun?. "))
for i in range(1,tekrar+1,1):
    print("dik üçgen, eşkenar üçgen, kare, dikdörtgen ya da daire seç...")
    print()
    tur=input("hangi şekli istiyorsun ")

    if tur=="dik üçgen":
        satır=int(input("üçgen satır satısını giriniz : "))
        for sayi in range(1,satır+1,1):
            print(sayi*"*")
    elif tur=="eşkenar üçgen":
        satır=int(input("üçgen satır sayısını giriniz : "))
        sayac = satır
        for sayi in range(1,satır+1):
            print(sayac*" ",(2*sayi-1)*"*")
            sayac-=1
    elif tur == "kare":
        satır = int(input("kare satır sayısını giriniz"))
        for dis in range(1,satır+1):
            for ic in range(1,satır+1):
                print("*", end=" ")
            print()
    elif tur=="dikdörtgen":
        satır=int(input("dikdörtgen sayır sayısını giriniz : "))
        sutun=int(input("dikdörtgen sütun sayısını giriniz : "))
        for satır in range(1,satır+1):
            for sutun in range(1,sutun+1):
                print("*", end=" ")
            print()
    elif tur =="daire":
        satır = int(input("daire satır sayısını giriniz"))
        for sayi in range(satır):   
            if sayi>satır/2:
                for k in range(satır-sayi):
                    print(" ",end="")
                for m in range((sayi+2)*2-1):
                    print("*",end="")
                print()
        for sayi in range(satır,0,-1):
            if sayi > satır/2:
                for k in range(satır-sayi):
                    print(" ",end="")
                for m in range((sayi+2)*2-1):
                    print("*",end="")
                print()
    else:
            print("dik üçgen, eşkenar üçgen, kare, dikdörtgen ya da daireseçebilirsiniz.")
            print()            