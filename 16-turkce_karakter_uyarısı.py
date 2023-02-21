def yildiz_ucgen_ciz():
  a=int(input("satır sayısı giriniz"))
  b=int(input("sutun sayısı giriniz"))
  for satir in range(0,a+1):   
    print("*" * satir)
    for sutun in range(0,b,a-1):
        print("*" * sutun)
       

yildiz_ucgen_ciz()