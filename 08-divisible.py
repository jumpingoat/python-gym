liczba = int(input('Podaj liczbę '))

if liczba % 5 == 0 and liczba % 11 == 0:
    print(f'Liczba {liczba} jest podzielna przez 5 i 11');
elif liczba % 5 ==0 and liczba % 11 != 0:
    print(f'Liczba {liczba} jest podzielna przez 5');
elif liczba % 5 != 0 and liczba % 11 == 0:
    print(f'Liczba {liczba} jest podzielna przez 11');
else:
    print(f'Liczba {liczba} nie jest podzielna przez 5 ani przez 11')
