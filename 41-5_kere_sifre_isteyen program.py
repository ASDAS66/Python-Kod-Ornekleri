
# Mustafa telefonuna 5 kere parola isteme özelliği eklemiştir. Telefon
# giriş yapmak için 5 kere parola istemektedir. Buna göre 5 kere parola
# isteyen Python kodu nasıl olmalıdır?
for sayi in range(1, 6, 1):
 cevap = int(input("Parola giriniz."))
 if cevap == 123:
    print("Girdiğiniz parola doğru")
 else:
    print("Girdiğiniz parola yanlış")