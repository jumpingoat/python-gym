# # Jedna z najprostszych wersji programu. Przyjmuje wartość wzrostu w centymetrach.
#
# height = int(input("What's your height in cm? "))
# weight = float(input("What's your weight in kg? "))
#
# # Ponieważ wartość wzrostu podana została w centymetrach, a potrzebujemy metrów, w nawiasie zamieniamy cm na m.
# bmi = weight / (height / 100) ** 2
#
# # Wypluwamy wynik
# print(bmi)

# Komplikujemy nasz program. Wprowadzamy możliwość wpisania wzrostu zarówno w centrymetrach jak i w metrach.
# Zamieniamy typ integer na float:
height = float(input("What's your height? "))
weight = float(input("What's your weight in kg? "))

# Teraz mamy dwie możliwości: albo user wpisał metry albo centymetry,
# ale człowiek generalnie nie powinien być wyższy niż 2.5 m
# Jeżeli podana liczba jest większa niż 2.5 to podany został wzrost w cm:
if (height) > 2.5:
    bmi = (weight / (height / 100) ** 2)
#W przeciwnym razie wzrost był w m i nie musimy ich dodatkowo wyliczać
# Funkcja round zaokrągla do dwóch miejsc po przecinku:
else:
    bmi = round(weight / (height**2), 2)

#Wypluwamy wynik
print(bmi)

