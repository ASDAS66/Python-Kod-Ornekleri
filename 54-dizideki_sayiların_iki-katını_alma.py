liste=[1,2,3,4,5,60]

def iki_kat_al(liste):
    i=0
    while i<len(liste):
        liste[i]=liste[i]*2
        i+=1
    return liste

yeni_liste=iki_kat_al(liste)
print(f"yeni liste : {yeni_liste}")