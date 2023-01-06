#girilen boya göre yorum yapabilen python kodu
boy=int(input("Boyunuzu giriniz : "))
if boy<160:
    print("Boyunuz çok kısa.")
elif boy<180:
    print("Boyunuz normal...")
elif boy<200:
    print("Boyunuz uzun")
else:
    print("boyunuz çok uzun sulak yerde mi büyüdün mübarek.")