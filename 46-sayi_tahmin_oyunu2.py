from random import randint

kolay_seviye_hak=10
zor_seviye_hak=5

#tahmini kontrol edelim
def tahminKontrol(senin_tahminin, tutulan_sayi,hak):
    if senin_tahminin<tutulan_sayi:
        print("daha büyük sayı giriniz")
        return hak-1
    elif senin_tahminin>tutulan_sayi:
        print("daha küçük bir sayı giriniz")
        return hak-1
    else:
        print("tebrikler kazandınız")

def zorluk_derecesi():
    seviye=input("zorluk derecesiniseçiniz zor kolay")
    if seviye=="zor":
        print("5 hakkın var")
        return zor_seviye_hak
    elif seviye=="kolay":
        print("10 hakkın var")
        return kolay_seviye_hak
def tahmin_oyunu():
    print("bilgisayar 1 ile 100 arasında bir sayı tuttu...")
    bilgtuttu=randint(1,100)

    hak=zorluk_derecesi()
    senin_tahminin=0
    while senin_tahminin!=bilgtuttu:
        print(f"kalan tahmin hakkın {hak}")
        senin_tahminin=int(input("senin tahminin ne?"))
        hak=tahminKontrol(senin_tahminin,bilgtuttu,hak)
        if hak==0:
            print("hakkın bitti")
            return
tahmin_oyunu()
    