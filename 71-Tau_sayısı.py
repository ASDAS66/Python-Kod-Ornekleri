#Klavyeden girilen sayının Tau Sayısı olup olmadığını tespit eden yazılımı python dilinde programlayınız
#Alime Beyza Arslan 16008118047
beyza_sayi=int(input("Beyza sayinizi gir: "))
beyza_bolen_sayisi=0
for beyza_n in range(beyza_sayi,0,-1):
    if beyza_sayi%beyza_n==0:
        beyza_bolen_sayisi+=1
if beyza_sayi%beyza_bolen_sayisi==0:
    print("beyza bu sayi tau sayisidir.")
else:
    print("beyza bu sayi tau sayisi değildir. ")
