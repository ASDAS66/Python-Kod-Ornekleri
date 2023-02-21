#saat yedi oldugunda alarm veren python kodu
saat=int(input("saati giriniz : "))

if saat<7 or saat>7:
    print("Uyumaya devam edin...")
elif saat==7:
    print("Alarm çalıyor, uyaann...")
else:
    print("lütfen bir saat giriniz...")