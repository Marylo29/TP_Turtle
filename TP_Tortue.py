import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed
s.colormode(255)

def equilateral(longueur):
    polygone(longueur,3)

def carre(longueur):
    polygone(longueur,4)


def polygone(longueur,nb_cotes,ajout=0,deviation=0,r=0,g=0,b=0,r_add=0,g_add=0,b_add=0):
    angle = (360/nb_cotes) - deviation
    for _ in range(nb_cotes):
        r= r+r_add if (r+r_add<=255) else r+r_add-256
        g= g+g_add if (g+g_add<=255) else g+g_add-256
        b= b+b_add if (b+b_add<=255) else b+b_add-256
        t.color(r,g,b)
        longueur += ajout
        t.forward(longueur)
        t.right(angle)

def figure1():
    polygone(2,150,3,-86.3,102,0,255,g_add=2)

def figure2():
    longueur = 2
    for _ in range(100):
        carre(longueur)
        t.right(10)
        longueur += 2



figure1()

turtle.exitonclick()