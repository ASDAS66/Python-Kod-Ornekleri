  #Kullanıcıdan alınan bir sayının "Armstrong" sayısı olup olmadığını bulan yazılımı python dilinde programlayınız.

#Alime Beyza Arslan 16008118047

beyza_arm=input("Sayi gir: ")
beyza_top=0
for beyza_i in range(len(beyza_arm)):
    beyza_top+=int(beyza_arm[beyza_i])**len(beyza_arm)
if beyza_top==int(beyza_arm):
    print(beyza_arm,"Beyza bu sayi armstrong sayisidir.")
else:
    print(beyza_arm,"Beyza bu sayi armstrong sayisi degildir.")  
