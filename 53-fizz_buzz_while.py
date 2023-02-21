sayi=1
while sayi<101:
    if sayi%3==0 and sayi%5==0:
        print("fizzbuzz")
    elif sayi%3==0:
        print("fizz")
    elif sayi%5==0:
        print("buzz")
    else:
        print(sayi)
    sayi+=1