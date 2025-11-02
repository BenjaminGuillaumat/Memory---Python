## Code des formes de bases ##

## Benjamin Guillaumat G3 ##

#####################################################################
#                       LES FORMES DE BASES                         #
#####################################################################


###################    Importation des modules    ###################

from turtle import *
import time
import turtle


#####################################################################
#                          LES FONCTIONS                            #
#####################################################################

def dessinePolygone(x,y,l,t,c,n):
    """ Dessine un polygones """
    t.up()
    t.color(c)
    t.width(3)
    t.goto(x,y)
    t.down()
    t.begin_fill()
    for i in range(0,n):
        t.forward(l)
        t.left(360/n)
    t.end_fill()


def carre(x,y,l,t,c):
    """ Dessine un carré """
    t.begin_fill()
    dessinePolygone(x,y,l,t,c,4)
    t.end_fill()


def triangle(x,y,l,t,c,direction):
    """ Dessine un triangle """
    t.begin_fill()
    t.left(direction)
    dessinePolygone(x,y,l,t,c,3)
    t.right(direction)
    t.end_fill()


def trait(x,y,l,epaisseur,c,t,direction):
    """ Dessine un trait """
    t.up()
    t.color(c)
    t.width(epaisseur)
    t.goto(x,y)
    t.down()
    t.left(direction)
    t.forward(l)
    t.right(direction)


def rectangle(x,y,h,L,t,c,direction):
    """ Dessine un rectangle """
    t.up()
    t.color(c)
    t.width(3)
    t.goto(x,y)
    t.down()
    t.begin_fill()
    l = [L,h,L,h]
    t.left(direction)
    for i in l: 
        t.forward(i)
        t.left(360/4)
    t.right(direction)
    t.end_fill()


def disque(x,y,r,t,c):
    """ Dessine un disque """
    t.up()
    t.color(c)
    t.width(6)
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.circle(r)
    t.end_fill()


def cercle(x,y,r,t,c,epaisseur):
    """ Dessine un cercle """
    t.up()
    t.color(c)
    t.width(epaisseur)
    t.goto(x,y)
    t.down()
    t.circle(r)


def arc_de_cercle_botte(x,y,r,t,c,epaisseur,direction):
    """ Dessine un arc de cercle pour la botte """
    t.up()
    t.color(c)
    t.width(epaisseur)
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.left(direction)
    t.circle(r,180)
    t.right(direction)
    t.end_fill()


def arc_de_cercle_boule(x,y,r,t,c,epaisseur,direction):
    """ Dessine un arc de cercle pour la boule de noël """
    t.up()
    t.color(c)
    t.width(epaisseur)
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.left(direction)
    t.circle(r,180)
    t.left(direction)
    t.end_fill()
