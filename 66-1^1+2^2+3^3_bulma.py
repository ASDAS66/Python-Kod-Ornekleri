#Klavyeden girilecek n sayısı için 1^1+2^2+3^3+…..nn değerini hesaplayan yazılımı python dilinde yazınız.

#Alime Beyza Arslan 16008118047
beyza_a=int(input("bir sayi giriniz : "))
liste=[]

for beyza_i in range(1,beyza_a):
    for beyza_m in range(1,beyza_a):
        beyza_x=beyza_m**beyza_i
        liste.append(beyza_x)
print("Beyza'nin buldugu sonuc",sum(liste))
