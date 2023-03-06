Beyza_i = 2
Beyza_sayı = int(input("Sayiyi giriniz: "))
Beyza_liste=[]
Beyza_çarpan=[]

while Beyza_i < Beyza_sayı:

    if Beyza_sayı % Beyza_i == 0:
        print(Beyza_i)
        Beyza_liste.append(Beyza_i)
    Beyza_i += 1
del Beyza_i
#print(liste)
for Beyza_i in Beyza_liste:
    Beyza_bitir=True
    for Beyza_a in Beyza_liste:
        if (Beyza_bitir):
            if(Beyza_i==Beyza_a):
                Beyza_çarpan.append(Beyza_i)
            elif(Beyza_i%Beyza_a==0):
                Beyza_bitir=False
       
print("\n",*Beyza_çarpan)
