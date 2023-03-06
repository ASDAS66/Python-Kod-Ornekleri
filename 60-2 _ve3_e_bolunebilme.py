#2 veya 3'e tam bölünebilen 10000'dan küçük kaç adet sayı olduğunu bulan yazılımı python dilinde yazınız.

#Alime Beyza Arslan 16008118047
beyza_k=[]
for beyza_i in range(1,10000):
    if beyza_i%2==0 and beyza_i%3:
        beyza_k.append(beyza_i)
print("Beyza'nın buldugu sonuc",beyza_k)
