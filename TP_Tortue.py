import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed

def equilateral(longueur):
    polygone(longueur,3)

def carre(longueur):
    polygone(longueur,4)


def polygone(longueur,nb_cotes,ajout=0,deviation=0):
    angle = (360/nb_cotes) - deviation
    for _ in range(nb_cotes):
        longueur += ajout
        t.forward(longueur)
        t.right(angle)

def figure1():
    polygone(2,150,3,-86.3)

def figure2():
    longueur = 2
    for _ in range(100):
        carre(longueur)
        t.right(10)
        longueur += 2



figure2()

turtle.exitonclick()