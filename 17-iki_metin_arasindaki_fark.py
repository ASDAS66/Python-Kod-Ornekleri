# ilk metinde olan ama ikinci metinde olmayan ögeleri yazdıran python kodu
ilk_metin="Bilgisayar"
ikinci_metin="Beyza"
for s in ilk_metin:
    if s in ikinci_metin:
        print("s", end=" , ")