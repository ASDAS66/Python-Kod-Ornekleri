beyza_girilenSayi = int(input("Beyza 2lik sisteme cevirilecek sayiyi gir: "))

beyza_cevrilenSayi = ""
while True: 
    if beyza_girilenSayi > 1: 
        beyza_cevrilenSayi = beyza_cevrilenSayi + str(beyza_girilenSayi % 2) 
        beyza_girilenSayi = beyza_girilenSayi // 2 
      
    elif beyza_girilenSayi == 1: 
        beyza_cevrilenSayi = beyza_cevrilenSayi + str(beyza_girilenSayi) 
        

    elif beyza_girilenSayi == 0: 
        beyza_cevrilenSayi = beyza_cevrilenSayi + str(beyza_girilenSayi)
        print(beyza_cevrilenSayi[::-1])
        break

    else:
        print("Beyza Lütfen bir DOGAL SAYI gir!")
        break 
input()
