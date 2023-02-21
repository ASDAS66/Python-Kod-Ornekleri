
import math

t=0
v=50
g=9.81
liste=[]

for t in np.orange(0,20,0.5):
    x=v*math.cos(60*math.pi/180)*t
    y=v*math.sin(60*math.pi/180)*t-0.5*g*t*t
    liste.append(y)
    print(f"yatayda aldığı yol: {x}\ndüşeyde aldığı yol:{y}\n")
    t+=0.5
print("maksimum yükseklik: ",max(liste))