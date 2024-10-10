#===================Zadanie 1==========================

name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
name_dictionary = {}

for item in name_list:
  name_dictionary[item] = len(item)
print(name_dictionary)


#==============Zadanie 2=========================

numbers = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
prime_numbers = []

for number in numbers:
    is_prime = False  
    for n in range(2, number):
        if number % n == 0:
            # is_prime = True
            break
    # if not is_prime:
    else:
        prime_numbers.append(number)

print(prime_numbers)


#=============Zadanie 3===============

week = ['pon','śro','pią','sob']
week.extend(['wto', 'czw', 'nie'])
print(week)

#Zabawy z lambdą i GPT. Wiem co to robi, ale na razie ryje mi beret. Niemniej pomysł wzorcowej listy, z której można by wyciąć pierwsze trzy litery dla porównania porządku jest mój własny ;)

correct_order = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
week_sorted = sorted(week, key=lambda day: [d[:3] for d in correct_order].index(day))
print(week_sorted)

#Wracam do insertów
week2 = ['pon','śro','pią','sob']
week2.insert(1, 'wto')
week2.insert(3, 'czw')
week2.insert(6, 'nie')
print(week2)

#=================Zadanie 4=================

herbata = ['włącz czajnik', 
'znajdź opakowanie herbaty', 
'zalej herbatę', 
'nalej wody do czajnika',
'wyjmij kubek', 
'włóż herbatę do kubka'] 

herbata[4], herbata[0] = herbata[0], herbata[4]
herbata[4], herbata[2] = herbata[2], herbata[4]
herbata[2], herbata[3] = herbata[3], herbata[2]
herbata[4], herbata[5] = herbata[5], herbata[4]

print(herbata)
print(" ")

print(r'''
               \.   \.      __,-"-.__      ./   ./
           \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
            \`.  \_`-''      _,="=._      ``-'_/  .'/
             \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
          \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
           \`-'  /    `-._  "       "  _.-'    \  `-'/
           /)   (         \    ,-.    /         )   (\
        ,-'"     `-.       \  /   \  /       .-'     "`-,
      ,'_._         `-.____/ /  _  \ \____.-'         _._`,
     /,'   `.                \_/ \_/                .'   `,\
    /'       )                  _                  (       `\
            /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \
           / ,-'        \/|`|`|`|'|'|'|\/        `-, \
          /,'             | | | | | | |             `,\
         /'               ` | | | | | '               `\
                            ` | | | '
                              ` | '
''')


