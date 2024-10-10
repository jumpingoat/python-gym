
# for i in range(1,6):
#     print("* " * 11)
#     print(" *" * 11)

# print(" ")

# for i in range(1,5):
#   for j in range(1,3):
#     print(str("*" * (i * 2)))

# print(" ")

# for i in range(7,0, -1):
#   print(str("*" * i))

# print(" ")

# n = 5  # liczba poziomów choinki
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '* ' * i)

ser1 = "roquefort"
ser2 = "stilton"
ser3 = "brie"
ser4 = "gouda"
ser5 = "edam"
ser6 = "parmezan"
ser7 = "mozzarella"
ser8 = "ser z owczego mleka"
deser = "listek miętowy"

masa1 = 2
masa2 = 1
masa3 = 1
masa4 = 1
masa5 = 1
masa6 = 3.5
masa7 = 0.13
masa8 = 0.22
masa9 = 0.2

cena1 = 12.50
cena2 = 11.24
cena3 = 9.30
cena4 = 8.55
cena5 = 11.00
cena6 = 16.50
cena7 = 14.00
cena8 = 122.32
cena9 = 20.00

print(f"{'Kolejny zajebisty ser':<22}{'|':^3}{'Masa (kg)|':<10}{'|':^3}{'Cena (zł)':<10}")
print("-----------------------------------------------")
print(f"{ser1:<22}{'|':^3}{masa1:<10}{'|':^3}{cena1:>6.2f}")
print(f"{ser2:<22}{'|':^3}{masa2:<10}{'|':^3}{cena2:>6.2f}")
print(f"{ser3:<22}{'|':^3}{masa3:<10}{'|':^3}{cena3:>6.2f}")
print(f"{ser4:<22}{'|':^3}{masa4:<10}{'|':^3}{cena4:>6.2f}")
print(f"{ser5:<22}{'|':^3}{masa5:<10}{'|':^3}{cena5:>6.2f}")
print(f"{ser6:<22}{'|':^3}{masa6:<10}{'|':^3}{cena6:>6.2f}")
print(f"{ser7:<22}{'|':^3}{masa6:<10}{'|':^3}{cena7:>6.2f}")
print(f"{ser8:<22}{'|':^3}{masa8:<10}{'|':^3}{cena8:>6.2f}")
print(f"{deser:<22}{'|':^3}{masa9:<10}{'|':^3}{cena9:>6.2f}")

print("-----------------------------------------------")
cena_zbiorcza = cena1 + cena2 + cena3 + cena4 + cena5 + cena6 + cena7 + cena8 + cena9
print(f"{'Rozpusta całkowita:':<19}{cena_zbiorcza:>25.2f}{' zł'}")


