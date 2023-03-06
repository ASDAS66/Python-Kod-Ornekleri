#fibonacci,Bu serinin dört milyondan küçük tüm çift sayılarının toplamını hesaplayan yazılımı python dilinde yazınız.

#Alime Beyza Arslan 16008118047
beyza_number = 0
beyza_previous = 1
beyza_total = 0

while beyza_number <= 4000000:
   beyza_fibonacci = beyza_previous + beyza_number
   beyza_number = beyza_fibonacci
   beyza_previous = beyza_fibonacci - beyza_previous

   if beyza_fibonacci % 2 == 0:
      beyza_total += beyza_fibonacci

print("Beyzanin buldugu sonuc: ", beyza_total)
