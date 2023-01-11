eposta="mail@python.com"
parola="1234abc"

girilen_eposta=input("lütfen e postanızı giriniz...")

if(girilen_eposta==eposta):
    girilen_parola=input("lütfen şifrenizi giriniz")
    if(girilen_parola==parola):
        print("giriş başarılı")
    else:
        print("girilen parola yanlış")
else:
    print("girilen e posta yanlış")