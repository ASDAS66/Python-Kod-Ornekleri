kacSatir=int(input("satır giriniz"))
for satirSayisi in range(1,kacSatir+1):
        print("*" * satirSayisi+" "* ((kacSatir-satirSayisi)*2) + "*"*satirSayisi)
for satirSayisi in range(1,kacSatir+1):
        print("*" * (kacSatir-satirSayisi)+" "* (satirSayisi*2) + "*"*(kacSatir-satirSayisi))
