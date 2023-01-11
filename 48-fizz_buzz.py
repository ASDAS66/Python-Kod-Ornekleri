#Sayı 3’e bölündüğünde, (örneğin 3) sayıyı yazdırmak yerine “Fizz” yazmalıdır.
# Sayı 5’e bölünebiliyorsa, (örneğin 5) sayıyı yazdırmak yerine “Buzz” yazmalıdır.
# Ve eğer sayı hem 3’e hem de 5’e bölünebiliyorsa, (örneğin 15) sayıyı yazdırmak yerine
#“FizzBuzz” yazmalıdır.

for sayi in range(1,101):
    if sayi%3==0 and sayi%5==0:
        print("fizzbuzz")
    elif sayi%3==0:
        print("fizz")
    elif sayi%5==0:
        print("buzz")
    else:
        print(sayi)
