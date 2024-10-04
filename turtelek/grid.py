import turtle

# Funkcja do rysowania siatki współrzędnych z oznaczeniami liczbowymi co 10 jednostek

# Ustawienia ekranu
window = turtle.Screen()
window.bgcolor("white")

#Funkcja definiująca żółwia, który narysuje siatkę
def rysuj_siatke(krok, rozmiar):
    brian = turtle.Turtle()
    brian.speed(0)
    brian.color("lightgray")
    brian.shape("square")
    
    # Rysowanie linii poziomych
    for y in range(-rozmiar, rozmiar + 1, krok):
        brian.penup()
        brian.goto(-rozmiar, y)
        brian.pendown()
        brian.goto(rozmiar, y)
        # Dodanie oznaczeń liczbowych wzdłuż osi Y
        if y % 50 == 0:  # Oznaczenia liczbowe co 50 jednostek dla czytelności
            brian.penup()
            brian.goto(-rozmiar - 20, y - 5)
            brian.write(y, align="right", font=("Arial", 8, "normal"))
    
    # Rysowanie linii pionowych
    for x in range(-rozmiar, rozmiar + 1, krok):
        brian.penup()
        brian.goto(x, -rozmiar)
        brian.pendown()
        brian.goto(x, rozmiar)

        # Dodanie oznaczeń liczbowych wzdłuż osi X
        if x % 50 == 0:  # Oznaczenia liczbowe co 50 jednostek dla czytelności
            brian.penup()
            brian.goto(x - 10, -rozmiar - 20)
            brian.write(x, align="center", font=("Arial", 8, "normal"))
    
    # Rysowanie osi X i Y
    brian.color("black")
    brian.penup()
    brian.goto(-rozmiar, 0)
    brian.pendown()
    brian.goto(rozmiar, 0)
    
    brian.penup()
    brian.goto(0, -rozmiar)
    brian.pendown()
    brian.goto(0, rozmiar)
    
    # Oznaczenie środka (0, 0)
    brian.penup()
    brian.goto(-10, -10)
    brian.write("0", align="center", font=("Arial", 8, "normal"))
    
    brian.hideturtle()

# Parametry siatki
krok_siatki = 10  # Odstęp między liniami siatki (co 10 jednostek)
rozmiar_siatki = 200  # Rozmiar siatki (maksymalny zakres współrzędnych w turtle to 200)

# Rysowanie siatki z oznaczeniami
rysuj_siatke(krok_siatki, rozmiar_siatki)

#turtle.mainloop()