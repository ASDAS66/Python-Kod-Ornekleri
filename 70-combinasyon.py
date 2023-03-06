# Klavyeden girilen 2 sayının combinasyonunu hesaplayan yazılımı python dilinde yazınız.

#Alime Beyza Arslan 16008118047
import math

while True:
    beyza_x = input("beyaz 1. sayıyı gir: ")
    if beyza_x=='q':
        break
    beyza_y = input("beyza 2. sayıyı gir: ")
    if beyza_y=='q':
        break
    try:
        fakx=math.factorial(int(beyza_x))
        faky=math.factorial(int(beyza_y))
        fakxy=math.factorial(int(beyza_x)-int(beyza_y))
        kom=int(fakx / (faky*fakxy))
        print("{} sayısının {} sayısıyla kombinasyonu: {}".format(beyza_x,beyza_y,kom))
    except ValueError:
        print("Lütfen uygun format kullanınız! (1.sayı > 2.sayı olmalı.)")
