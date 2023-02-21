kacSatir=int(input("satir sayisi giriniz..."))
for satirSayisi in range(1,kacSatir+1):
       print("*" * satirSayisi+" "* ((kacSatir-satirSayisi)*2) + "*"*satirSayisi)
