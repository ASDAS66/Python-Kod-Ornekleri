#1000'den küçük tüm hilbert sayılarını listeleyen yazılımı python dilinde yazınız.
#Alime Beyza Arslan 16008118047

beyza_hilbert=[]
for beyza_i in range(1,1000):
    if (beyza_i-1)%4==0 :
        beyza_hilbert.append(beyza_i)
print("Beyza hilbert sayilari listesi : ",beyza_hilbert,len(beyza_hilbert)," tane hilbert sayisi vardir..")
