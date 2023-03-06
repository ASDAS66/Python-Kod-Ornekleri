#1'den 10'a kadar olan tüm sayıların 100'e kadar olan ritmik sayılar tablosunu iç-içe döngü yapılarını kullanarak python dilinde kodlayınız

#Alime Beyza Arslan 16008118047
print("Beyza'nin sonucu : \n")
for beyza_i in range(2,11):
    for beyza_j in range(1,101):
        if beyza_j % beyza_i == 0:
            print(beyza_j,end=" ")
    print("\n")
