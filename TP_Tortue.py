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
        t.left(angle)
def figure1():
    polygone(2,150,3,-86.3)

def figure2():
    for i in range(0,200,5):
        polygone(10+i,4)

figure2()

turtle.exitonclick()