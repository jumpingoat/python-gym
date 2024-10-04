pierwsza = float(input('Podaj wartość pierwszą '))
druga = float(input('Podaj wartość drugą '))

if pierwsza > druga:
    print(f'Liczba {pierwsza} jest większa od liczby {druga}');
elif pierwsza == druga:
    print(f'Liczba {pierwsza} jest równa liczbie {druga}');
else:
    print(f'Liczba {pierwsza} jest mniejsza od liczby {druga}')