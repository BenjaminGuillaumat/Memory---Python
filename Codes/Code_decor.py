## Code du décor du Memory ##

## Benjamin Guillaumat G3 ##


#####################################################################
#                              LE DECOR                             #
#####################################################################


###################    Importation des modules    ###################

from turtle import *
from Code_formes import *
from math import *
import random


#####################################################################
#                          LES FONCTIONS                            #
#####################################################################


def traineau1(x,y,t):
    """ Dessine le traineau de gauche """
    h = 200
    L = 300
    #rails du traineau
    trait(x+200,y+200,30,10,"yellow",t,315)
    trait(x+100,y+50,230,10,"yellow",t,45)
    trait(x+265,y+215,50,10,"yellow",t,80)
    update()
    #corps du traineau
    rectangle(x,y,h,L,t,"red",45)
    rectangle(x+213,y+213,h*1/3,L*1/3,t,"red",80)
    rectangle(x+230,y+310,h*1/2,L*5/8,t,"red",135)


def traineau2(x,y,t):
    """ Dessine le traineau de droite """
    h = 200
    L = 300
    #rails du traineau
    trait(x-340,y+60,30,10,"yellow",t,225)
    trait(x-250,y-80,218,10,"yellow",t,135)
    trait(x-405,y+75,50,10,"yellow",t,100)
    update()
    #corps du traineau
    rectangle(x,y,h,L,t,"red",135)
    rectangle(x-290,y+85,h*1/3,L*1/3,t,"red",100)
    rectangle(x-303,y+101,h*1/2,L*5/8,t,"red",45)


def cadeau(x,y,t,L,h):
    """ Dessine un cadeau """
    rectangle(x,y,h,L,t,"red",0)
    trait(x,y+((2/3)*h),L,5,"black",t,0)
    rectangle(x+L/6,y,h,(L/6),t,"black",0)
    carre(x+(L/2-L/16),y+h,L/8,t,"yellow")
    triangle(x+(L/2-L/16),y+(h+L/16),15,t,"yellow",135)
    triangle(x+(L/2+L/16),y+(h+L/16),15,t,"yellow",315)


def montagne(x,y,t):
    """ Dessine une montagne """
    #montagne
    triangle(x,y,200000,t,"#836D68",240)
    #neige
    rectangle(x-60,y-50,80,300,t,"white",315)
    rectangle(x-110,y-100,72,200,t,"white",315)
    rectangle(x-160,y-150,72,100,t,"white",315)
    rectangle(x-210,y-200,72,50,t,"white",315)


def lune(x,y,t):
    """ Dessine la lune """
    rayon = 200
    #lune
    disque(x,y,rayon,t,"white")
    #traineau
    rectangle(x+100,y+175,20,35,t,"black",340)
    disque(x+130,y+180,5,t,"black")
    trait(x+95,y+170,45,2,"black",t,340)
    trait(x+138,y+155,7,2,"black",t,15)
    trait(x+95,y+170,7,2,"black",t,115)
    trait(x+103,y+168,7,2,"black",t,70)
    trait(x+127,y+159,7,2,"black",t,70)
    #reines
    trait(x+110,y+185,25,2,"black",t,180)
    disque(x+80,y+180,5,t,"black")
    trait(x+75,y+185,25,2,"black",t,200)
    disque(x+50,y+170,5,t,"black")
    trait(x+50,y+175,25,2,"black",t,215)
    disque(x+25,y+152,5,t,"black")
    trait(x+25,y+158,25,2,"black",t,225)
    disque(x+5,y+132,5,t,"black")
    trait(x+2,y+132,25,2,"black",t,235)
    disque(x-12,y+108,5,t,"black")


def bdn(x,y,t):
    """ Dessine un bonhomme de neige """
    rayon1 = 60
    rayon2 = 30
    # Corps
    disque(x,y,rayon1,t,"white")
    disque(x,y+120,rayon2,t,"white")
    # Chapeau
    rectangle(x-25,y+170,15,50,t,"green",0)
    rectangle(x-20,y+185,25,40,t,"green",0)
    disque(x,y+190,5,t,"red")
    # Bras
    trait(x-45,y+90,70,5,"brown",t,225)
    trait(x+45,y+90,70,5,"brown",t,315)
    # Écharpe
    rectangle(x-25,y+115,15,50,t,"red",0)
    rectangle(x-10,y+125,15,50,t,"red",225)
    rectangle(x,y+120,10,40,t,"red",315)
    # Boutons
    disque(x,y+15,5,t,"black")
    disque(x,y+40,5,t,"black")
    disque(x,y+65,5,t,"black")
    # Yeux
    disque(x-10,y+155,2,t,"black")
    disque(x+10,y+155,2,t,"black")
    # nez
    trait(x,y+146,20,8,"orange",t,180)
    update()


def sapin(x,y,l,t,c):
    """ Dessine un sapin """
    couleur = ["Cyan","red","blue","yellow","purple"]
    #sapin
    trait(x+l//2,y,l//4,l*1/5,"#61281C",t,270)
    triangle(x,y,l,t,"green",0)
    triangle(x+(l/2-1/3*l),y+(2/3*l),(2/3*l),t,"green",0)
    #boules de noël
    disque(x+(l/3),y+(l/8),(l/24),t,random.choice(couleur))
    disque(x+(2/3*l),y+(l/4),(l/24),t,random.choice(couleur))
    disque(x+(2/5*l),y+(3/4*l),(l/24),t,random.choice(couleur))
    disque(x+(5/12*l),y+(7/16*l),(l/24),t,random.choice(couleur))
    disque(x+(9/16*l),y+(29/32*l),(l/24),t,random.choice(couleur))


################ Fonctions pour les flocons ###############


def branche(l,t):
    """ Dessine une branche d'un flocon """
    for i in range(3):
        for i in range(3):
            t.forward(l)
            t.backward(l)
            t.right(45)
        t.left(90)
        t.backward(l)
        t.left(45)
    t.right(90)
    t.forward(3*l)


def flocon(x,y,l,t,c):
    """Dessine un flocon """
    t.up()
    t.color(c)
    t.width(1)
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(8):
        branche(l,t)
        t.left(45)
    t.end_fill()


########## Fonctions des objets sous les cadeaux ##########


def bonbon(x,y,t,c):
    """ dessine un bonbon """
    #corps du bonbon et emballage
    r = 18
    disque(x+30,y+5,r,t,c)
    triangle(x+r+30,y+r+5,r,t,c,315)
    triangle(x-r+30,y+r+5,r,t,c,135)
    # MIAM
    t.up()
    t.goto(x-3/5*r+30,y+4/5*r+5)
    t.down()
    t.color("black")
    t.write("MIAM",font=("Arial",r//2, "normal"))


def petit_traineau(x,y,t,c):
    """ dessine un petit traineau de noël """
    #traineau
    t.color(c)
    rectangle(x+15,y+15,20,35,t,"black",340)
    disque(x+45,y+20,5,t,"black")
    trait(x+10,y+10,45,2,"black",t,340)
    trait(x+53,y-5,7,2,"black",t,15)
    trait(x+10,y+10,7,2,"black",t,115)
    trait(x+18,y+8,7,2,"black",t,70)
    trait(x+42,y-1,7,2,"black",t,70)


def botte(x,y,t,c):
    """ dessine une botte de noël """
    rectangle(x+20,y+20,12,30,t,c,45)
    arc_de_cercle_botte(x+13,y+27,15,t,c,5,225)
    arc_de_cercle_botte(x+34,y+6,10,t,c,5,225)
    rectangle(x+34,y+30,16,18,t,"white",45)


def boulenoel(x,y,t,c):
    """ Dessine une boule de noël """
    trait(x+30,y+34,20,5,"black",t,90)
    disque(x+30,y,18,t,c)
    arc_de_cercle_boule(x+30,y+54,5,t,"black",5,90)

