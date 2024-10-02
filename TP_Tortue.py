import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed

def equilateral(longueur):
    for i in range(3):
        t.forward(longueur)
        t.left(120)


equilateral(200)

def carre(longueur):
    for i in range(4):
        t.forward(longueur)
        t.left(90)

carre(200)
turtle.exitonclick()