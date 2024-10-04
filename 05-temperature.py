temperature = int(input('Podaj temperaturę na zewnątrz '))

if temperature <= 10:
    print('Zostań w domu')
elif temperature > 10 and temperature < 20:
    print('Ubierz się')
else:
    print('Baw się dobrze')