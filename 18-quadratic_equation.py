# Stwórz funkcję equation, która jako argumenty bierze zmienne a, b, c będące współczynnikami równania kwadratowego, a następnie oblicza rozwiązania tegoż równania.
# Podpowiedź W pierwszej kolejności, funkcja main na podstawie zadanych argumentów powinna obliczać wyróżnik równania kwadratowego - czyli znaną wszystkim ze szkoły średniej deltę.
# Następnie w zależności od tego, czy delta jest większa, równa lub mniejsza od 0 - funkcja powinna zwracać odpowiednio:
# Jeśli delta > 0: dwa rozwiązania x1 oraz x2. Niech funkcja zwraca je jako krotkę.
# Jeśli delta = 0: jedno rozwiązanie x0. Niech funkcja zwraca wtedy tylko tę zmienną.
# Jeśli delta < 0: brak rozwiązań. Niech funkcja zwraca wtedy tekst "Brak rozwiązań".
import math

def equation(a, b, c):
    delta = (b * b) - (4 * a * c)
    if delta == 0:
        x0 = - (b/2*a)
        print(f"Delta jest równa 0. Wynik to {x0}.")
    elif delta >0:
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        print(f"Delta jest większa od 0 i wynosi {delta}. Równanie posiada dwa rozwiązania: \n x1 = {x1}, \n x2 = {x2}.")
    else:
        print("Równanie nie posiada rozwiązań")


equation(2, 8, 6)

# 2, 8, 6 delta > 0
# 1, 2, 1 delta = 0
# 2, 2, 2 delta < 0



