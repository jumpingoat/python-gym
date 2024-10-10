# Do zmiennej names została przypisana lista imion męskich.
# Stwórz słownik, którego kluczami będą pierwsze litery imion w liście names, a wartościami będą wszystkie imiona, które zaczynają się na daną literę.
# Słownik przypisz do zmiennej name_dict.

# Na przykład: name_dict['P'] powinien zwracać imiona: Paweł, Piotr
# Podpowiedź: Miej na uwadze, że imiona w słowniku nie powinny się powtarzać!

names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}

for name in names:
    letter = name[0]
    if letter not in name_dict:
        name_dict[letter] = []
        name_dict[letter].append(name)
    else:
        name_dict[letter].append(name)

print(sorted(name_dict.items()))







