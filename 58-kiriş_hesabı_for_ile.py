import numpy as np
L=1
E=210*(10**9)
I=8.333*(10**(-5))
for P in np.orange (0, 10, 0.5): #range fonksiyonu float değer almadığı için np.arrange () kullanıldı
    y=-(P*L**3)/(3*E*I)
    P+=0.5
    print("Y değeri:",y)