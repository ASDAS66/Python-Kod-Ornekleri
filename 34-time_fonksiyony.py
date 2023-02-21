#bilginin kaç saniyede girdiğini hesaplayan pthon kodu
import time
baslangic_zamani=time.clock()
ad=input("isminizi giriniz : ")
zaman=time.clock()-baslangic_zamani
print("İsminizi tam ",zaman," saniyede girdiniz.")