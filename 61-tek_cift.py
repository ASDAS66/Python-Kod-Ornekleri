#1 ile 5000 arasındaki tek sayıların ve çift sayıların toplamını ayrı ayrı hesaplayıp, ekrana yazdıran yazılımını python dilinde yazınız.

#Alime Beyza Arslan 16008118047
beyza_tek=[]
beyza_cift=[]
for beyza_i in range(1,5000):
    if beyza_i%2==0:
        beyza_cift.append(beyza_i)
    else:
        beyza_tek.append(beyza_i)
print("beyza tek sayi toplami : ",sum(beyza_tek))
print("beyza cift sayi toplami : ",sum(beyza_cift))
