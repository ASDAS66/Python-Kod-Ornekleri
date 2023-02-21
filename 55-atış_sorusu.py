#Aşağıdaki formül ve verilerin ışığında Python ile atış problemi örneği derlenmiştir. Örnek
#aşağıdaki şekilde açıklanmıştır:
# 50 m/s başlangıç hızıyla ve yatay eksene 60° başlangıç açısıyla bir top fırlatılmıştır.
# Topun zaman 0 ile 20 saniye arasındaki 0,5’lik artışlarla değiştiğinde bir parçacığın
#yatay ve dikey konumunu belirleyen bir program yazın.
# Program ayrıca topun ulaşabileceği maksimum yüksekliği de görüntülesin.


#formül x=V0*cosa*t /// y=V0*sina*t-(1/2)g*t*t
import math

t=0
v=50
g=9.81
liste=[]
a="Hesaplama : "
print(a)
while t<=20:
    x=v*math.cos(60*math.pi/180)*t
    y=v*math.sin(60*math.pi/180)*t
    liste.append(y)
    print(f"yatayda aldığı yol:{x}\nDüşeyde aldığı yol:{y}\n")
    t+=0.5
print("maksimum yükseklik: ",max(liste))
