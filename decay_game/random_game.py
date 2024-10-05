import keyboard
import random
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

font = {'family': 'serif',
          'color': '#ff0066',
          'weight': 'bold',
          'size': 20,}

#x = int(input("do jakiej liczby liczyć? "))

#Losowanie liczby
x = random.randint(1, 10000)
y = 1
#Stworzenie tablicy, do której będą zapisywane liczby z losowania
numbers = []

#Zdefiniowanie obrazka do otworzenia na koniec gry
img = mpimg.imread('.\\no.png')


#Początek gry
print("Liczymy do " + str(x) + ". Zatrzymaj program dokładnie na tej liczbie.")

input("Naciśnij Enter, żeby rozpocząć")

while y:
    #Definicja klawisza zatrzymującego odliczanie
    if keyboard.is_pressed("q"):
        #Generowanie kolejnych liczb
        if (numbers[-1]) == x:
            print("Zajebiście!")
        else:
            print("Zdupiłeś!")
            #Schowaj układ współrzędnych w matplot i pokaż obrazek
            plt.axis('off')
            plt.title('You\'ve lost! Now you decay!', fontdict=font)
            plt.imshow(img)
            plt.show()

        break
    else:
        print(y)
        numbers.append(y)
        y = y + 1


#Opisanie wyświetlonego obrazka z matplolib - niech tam się pojawia info o zdupieniu
#W matplotlib ukryć układ współrzędnych
#Zrobić kolejny wykres: wylosowana liczba kontra odchylenie (różnica)
        #pomiędzy wylosowaną a zatrzymaną
        

