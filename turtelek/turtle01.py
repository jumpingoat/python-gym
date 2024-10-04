import turtle
#import grid


monty = turtle.Turtle()
monty.shape("arrow")
monty.speed(10)
monty.penup()
monty.goto(0, 0)
monty.pendown()

monty.left(90)

def tower(color, s1, s2, t1, t2, t3): 
    for _ in range(2):
        monty.pencolor(color)
        monty.fillcolor(color)
        monty.begin_fill()
        monty.forward(s1) 
        monty.right(90)
        monty.forward(s2) 
        monty.right(90)
        monty.end_fill()
    monty.pencolor('#ff0066') 
    monty.fillcolor('#ff0066')
    monty.begin_fill()
    monty.forward(s1) 
    monty.left(90)
    monty.forward(t1) 
    monty.right(135)
    monty.forward(t2) 
    monty.right(90)
    monty.forward(t2) 
    monty.right(135)
    monty.forward(t3) 
    monty.end_fill()

def main_wall(color, f1, f2):
        monty.pencolor(color) 
        monty.fillcolor(color)
        for i in range(2):
            monty.begin_fill()
            monty.forward(f1)
            monty.right(90)
            monty.forward(f2)
            monty.right(90)
            monty.end_fill()

def bricks(step, color): 
    monty.pencolor(color)
    monty.fillcolor(color)
    for i in range(step):
        monty.begin_fill()
        monty.forward(10)
        monty.right(90)
        monty.forward(10)
        monty.right(90)
        monty.forward(10)
        monty.left(90)
        monty.forward(10)
        monty.left(90)
        monty.end_fill()
        

def door(r, x, y, f1, f2):
    monty.pencolor('#663300')
    monty.fillcolor('#663300')
    monty.begin_fill()
    monty.circle(r)
    monty.end_fill()
    monty.penup()
    monty.goto(x, y)
    monty.right(90)
    monty.pendown()
    for i in range(2):
        monty.begin_fill()
        monty.forward(f1)
        monty.right(90)
        monty.forward(f2)
        monty.right(90)
    monty.forward(f1)
    monty.end_fill()
    monty.penup()

def big_triangle():
    monty.pencolor('#ff0066')
    monty.fillcolor('#ff0066')
    monty.begin_fill()
    monty.forward(10)
    direction(45)
    monty.forward(95)
    monty.right(90)
    monty.forward(95)
    direction(180)
    monty.forward(15)
    monty.end_fill()


def direction(angle):
     monty.setheading(angle)

def move(x, y):
     monty.penup()
     monty.goto(x, y)
     monty.pendown()

move(-180, -150)
main_wall('#ffa64d', 70, 310)
direction(90)
move(-130,-80)
main_wall('#ff8c1a', 50, 210)
direction(90)
move(-80, -30)
main_wall('#e67300', 70, 110)

move(-25, -100)
direction(180)
door(20, -45, -150, 30, 40)
move(-25, -50)
direction(180)
door(10, -35, -80, 20, 20)
move(-25, 0)
direction(180)
door(10, -35, -30, 20, 20)
direction(90)
move(-130, -30)
tower('#e67300', 60, 30, 15, 40, 39.5)
move(50, -30)
direction(90)
tower('#e67300', 60, 30, 15, 40, 39.5)

move(-130, -30)
direction(90)

bricks(11, '#ff8c1a')
monty.left(90)
monty.pencolor('white')
monty.forward(10)

move(-180, -80)
direction(90)

bricks(16, '#ffa64d', )
monty.left(90)
monty.pencolor('white')
monty.forward(10)

move(-150, -150)
direction(90)
tower('#ff9933', 100, 40, 15, 50, 55)

move(60, -150)
direction(90)
tower('#ff9933', 100, 40, 15, 50, 55)

move(-80, 40)
direction(180)

big_triangle()

#okna
move(-60, 30)
direction(180)
door(5, -65, 15, 10, 10)

move(-25, 30)
direction(180)
door(5, -30, 15, 10, 10)

move(10, 30)
direction(180)
door(5, 5, 15, 10, 10)

move(-60, -40)
direction(180)
door(5, -65, -55, 10, 10)

move(15, -40)
direction(180)
door(5, 10, -55, 10, 10)

move(-60, -90)
direction(180)
door(5, -65, -105, 10, 10)

move(15, -90)
direction(180)
door(5, 10, -105, 10, 10)

move(-130, -60)
direction(180)
door(5, -135, -75, 10, 10)

move(80, -60)
direction(180)
door(5, 75, -75, 10, 10)

move(-115, 25)
direction(180)
door(5, -120, 10, 10, 10)

move(65, 25)
direction(180)
door(5, 60, 10, 10, 10)


monty.hideturtle()


turtle.mainloop()
