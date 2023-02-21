#manavdan alınanlara göre fiyat veren python kodu

meyve=input("---Hangi meyveyi istersiniz---")
if meyve==("muz"):
    kilo=int(input("Kaç kilo muz istiyorsunuz?..."))
    print(kilo*5," tl ödeme yapmanız gerekmektedir...")
elif meyve==("elma"):
    renk=input("Hangi renk elma istersiniz...")
    if renk==("kırmızı"):
        kilo=int(input("Kaç kilo kırmızı elma istersiniz?.."))
    elif renk==("sarı"):
        kilo=int(input("Kaç kilo sarı elma istiyorsunuz?.."))
    elif renk==("yeşil"):
        kilo=int(input("Kaç kilo yeşiilelma istiyorsunuz?.."))
    else:
        print("Manavımızda sadece kırmızı,yeşil ve sarı elma bulunmaktadır.")
    print(kilo*2, " tl ödeme yapmanız gerekmektedir...")
elif meyve==("üzüm"):
    renk=input("Hangi renk üzüm istiyorsunuz?..")
    if renk ==("mor"):
        kilo=int(input("Kaç kilo üzüm istiyorsunuz?.."))
    elif renk==("yeşil"):
        kilo=int(input("Kaç kilo yeşil üzüm istersiniz?.."))
    else:
        print("manavımızda sadece yeşil ve mor üzüm bulunmaktadır.")
    print(kilo*3.5," tl ödeme yapmanız gerekmektedir...")
else:
    print("Manavımızda sadece elma,muz ve üzüm bulunmaktadır...")