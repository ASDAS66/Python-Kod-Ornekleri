#0 ile 100 arasında rastgele sayı üretip, kullanıcının bu sayıyı tahmin etmesini isteyen ve kaç tahmin sonunda sayıyı bulduğunu kullanıcıya gösteren kod
import random
#Alime Beyza Arslan 16008118047
beyza_sayaç=0
beyza_sayı=random.randint(1,1000)

beyza_tahminler = []
while beyza_sayaç<20:
    beyza_tahmin = int(input("Beyza tahmin edilen sayı ne? :"))

    if  beyza_sayı>beyza_tahmin:
        print("beyza tahmin sayini yükselt...")
        beyza_tahminler.append(beyza_tahmin)
        beyza_sayaç += 1
        kalanhak = 20 - beyza_sayaç
        print("beyza kalan tahmin hakkin : ", kalanhak)
    elif beyza_sayı<beyza_tahmin:
        print("beyza tahmin sayisini düşür...")
        beyza_tahminler.append(beyza_tahmin)
        beyza_sayaç += 1
        kalanhak = 20 - beyza_sayaç
        print("beyza kalan tahmin hakkin : ", kalanhak)
 
    else:
        beyza_tahminler.append(beyza_tahmin)
        print("\nTebrikler, Doğru tahmin. \n")
        print("Yapilan Tahmin sayisi :",len(beyza_tahminler))
        print("Tahmin ettiğiniz sayilar : ",beyza_tahminler)
        break
