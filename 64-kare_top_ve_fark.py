#ilk 10 doğal sayının kareleri toplamı ile toplamlarının kareleri arasındaki farkı hesaplayan yazılımı python dilinde yazınız

#Alime Beyza Arslan 16008118047
beyza_karetoplistem=[]
for beyza_i in range(1,10):
    beyza_i=beyza_i**2
    beyza_karetoplistem.append(beyza_i)

beyza_toplamatoplistem=[]
for m in range(0,100):
    m=m+1
    beyza_toplamatoplistem.append(m)

print("sayilarin tek tek kareleri toplami : ",sum(beyza_karetoplistem))
print("sayilar toplaminin karesi : ",sum(beyza_toplamatoplistem)**2)

print("Beyza'nin sonucu :",sum(beyza_karetoplistem)-(sum(beyza_toplamatoplistem)**2))
