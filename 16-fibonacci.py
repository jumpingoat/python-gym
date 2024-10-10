# Ciąg Fibonacciego to sekwencja, w której każda kolejna liczba jest sumą dwóch poprzednich liczb.
# Na przykład: 1,1,2,3,5,8,13...

# Napisz program, który zwraca listę kolejnych 30 elementów ciągu Fibonacciego. Listę zawierającą kolejne elementy ciągu przypisz do zmiennej fibonacci

fibonacci = [0, 1]

for item in range(2, 30):
    val = ((fibonacci[item-1]) + (fibonacci[item-2]))
    fibonacci.append(val)

print(fibonacci)