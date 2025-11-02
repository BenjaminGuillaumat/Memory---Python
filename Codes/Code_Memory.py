## Code du Memory ##

## Benjamin Guillaumat G3 ##

###################    Importation des modules    ###################


from turtle import *
import time
from Code_formes import *
from Code_decor import *
from math import *
import random


################    Création des tortues (turtle)    ################


td = Turtle() # tortue du décor
td.hideturtle()
tc = Turtle() # tortue des cases (cadeaux)
tc.hideturtle()
tracer(0) # le dessin est instantané (on ne voit pas le déplacement de la tortue)


################    Création de la fenètre de jeu    ################


setup(1920,1080,0,0) #taille
bgcolor("#193684") #couleur de fond
title("Christmas Memory") #titre


#####################################################################
#                          LES FONCTIONS                            #
#####################################################################

def texte(texte,x,y,color,police,taille,t):
    """ Affiche un texte à l'écran avec la fonction turtle.write() """
    t.up()
    t.goto(x,y)
    t.color(color)
    t.down()
    t.write(texte,align = "center", font=(police, taille, "italic","bold"))

def decor(t):
    """ Dessine le décor avec la tortue t """
    #Montagnes
    montagne(-250,350,td)
    montagne(470,250,td)
    #Lune
    lune(-650,100,td)
    #Bonhomme de neige
    bdn(160,160,td)
    #Sapins
    sapin(-750,-100,100,td,0)
    sapin(-650,-20,60,td,0)
    sapin(-575,0,120,td,0)
    sapin(-450,-100,150,td,0)
    sapin(-300,0,60,td,0)
    sapin(-180,-40,120,td,0)
    sapin(-250,-150,120,td,0)
    sapin(-30,-20,100,td,0)
    sapin(100,-50,150,td,0)
    sapin(300,-100,150,td,0)
    sapin(450,0,60,td,0)
    sapin(550,-50,100,td,0)
    sapin(650,-100,60,td,0)
    sapin(-80,-120,80,td,0)
    sapin(0,-170,120,td,0)
    sapin(220,-170,120,td,0)
    sapin(-330,-190,80,td,0)
    #Flocons
    for i in range(100): #Les 100 flocons sont placés aléatoirement sur l'écran
        flocon(random.randrange(-650,800),random.randrange(-650,800),4,td,"cyan")
    #Traineaux
    traineau1(-680,-480,td)
    bdn(-575,-300,td)
    traineau2(800,-340,td)
    bdn(550,-300,td)
    #Fond barre de progression
    trait(-300,-350,600,15,"black",td,0)
    #Nombre de tentatives restantes
    carre(600,280,90,td,"white")
    texte("Tentatives restantes : ",430,310,"white","Arial",30,td)


def dessineCadeau(x,y,L,h,n,t):
    """ Dessine un cadeau avec un nombre dessus avec la tortue t """
    t.up()
    t.goto(x,y)
    t.down()
    # on trace un cadeau
    cadeau(x,y,t,L,h)
    # on se place pour écrire le chiffre i
    t.up()
    t.goto(x+L/2,y-2)
    t.down()
    t.color("white")
    t.write(str(n),font=('Arial',25,'normal'))


def fonc_difficulte(n):
    """ Choisi le nombre de tentative attribué en fonction de la difficulté choisi """
    if n == "Easy":
        return 12
    elif n == "Medium":
        return 8
    elif n == "Hard" :
        return 4


def score_actualisation():
    """ Efface les dessins de la tortue tc et actualise l'affichage de la barre de progression ainsi que le nombre de tentative restantes """
    trait(-300,-350,600*(nb_tentatives/fonc_difficulte(difficulte)),15,"red",tc,0)    # On actualise l'affichage de la barre de progression en bas de l'écran
    texte(nb_tentatives,642,295,"red","Arial",55,tc)    # On actualise l'affichage du nombre de tentative en haut de l'écran

    tc.clear()

    trait(-300,-350,600*(nb_tentatives/fonc_difficulte(difficulte)),15,"red",tc,0)    # On actualise l'affichage de la barre de progression en bas de l'écran
    texte(nb_tentatives,642,295,"red","Arial",55,tc)    # On actualise l'affichage du nombre de tentative en haut de l'écran


def etape() :
    global nb_tentatives
    """ Permet de demander deux cadeaux au choix à retourner par l'utilisateur.
        Les deux cadeaux sont remplacées par les objets correspondant.
        Les autres reste des cadeaux. """

    score_actualisation() #On actualise les dessins de tc

    for i in range (1,len(case)+1): 
        if trouver[i-1]==False:  # Si la paire de l'objet d'indice correspondant n'a pas été découvert alors on dessine le cadeau
            dessineCadeau(-488+i*100,-300,60,40,i,tc)
        else : # Sinon on dessine l'objet correspondant
            case[i-1][0](-488+i*100,-300,tc,case[i-1][1])
            update()




    # Premier choix
    choix1 = numinput("Quel est votre premier choix ?", "le numéro du cadeau")
    while choix1 > len(case) or choix1 <= 0: # Si le choix n'est pas bon donc pas entre 1 et 8 alors on redemande jusqu'à avoir un choix possible
        choix1 = numinput("Quel est votre premier choix ?", "le numéro du cadeau")

    score_actualisation() #On actualise les dessins de tc

    for i in range (1,len(case)+1): 
        if choix1 != i and trouver[i-1]==False: # Si l'indice ne correspond pas au choix du joueur ou si l'indice correspond à un objet d'une paire pas encore découverte, alors on dessine un cadeau
            dessineCadeau(-488+i*100,-300,60,40,i,tc)
        else : # Si l'indice correspond au choix du joueur ou si l'indice correspond à un objet d'une paire déjà découverte, alors on dessine l'objet correspondant
            case[i-1][0](-488+i*100,-300,tc,case[i-1][1])
            update()




    # Deuxième choix (les commentaires sont les mêmes que pour le choix 1)
    choix2 = numinput("Quel est votre second choix ?", "le numéro du cadeau")
    while choix2 > len(case) or choix2 <= 0:
        choix2 = numinput("Quel est votre second choix ?", "le numéro du cadeau")

    score_actualisation()

    for i in range (1,len(case)+1):
        if ((int(choix1) != i and choix2 != i) or choix1==choix2) and trouver[i-1]==False  : 
            dessineCadeau(-488+i*100,-300,60,40,i,tc)
        else :
            case[i-1][0](-488+i*100,-300,tc,case[i-1][1])
            update()





    # on attend 2 secondes avant de remettre les cases pour cacher
    time.sleep(2)
    tc.clear()

    if (case[int(choix1 -1)][0]==case[int(choix2 -1)][0]) and choix1 != choix2 : # Si une paire est découverte alors on met les élément d'indice correspondant au objet de la paire en "True" dans la liste "trouver"
        trouver[int(choix1 -1)]=True
        trouver[int(choix2 -1)]=True

    else : #Sinon on ne fait rien car aucune perd n'est découverte mais on perd une tentative
        tc.clear()
        nb_tentatives = nb_tentatives - 1

#####################################################################
#                           LE PROGRAMME                            #
#####################################################################


##############    Définition des différentes listes    ##############


couleurs = ["red","yellow","blue","purple"] #Listes de toutes les couleurs et des objets sous les cadeaux
objets = [bonbon,bonbon,botte,botte,petit_traineau,petit_traineau,boulenoel,boulenoel]

#Liste de tous les objets dans des positions aléatoires
case = []
for i in range(len(objets)):
    elt = [random.choice(objets),random.choice(couleurs)]
    case.append(elt)
    objets.remove(elt[0])

trouver =[False for i in range(len(case))] # Liste définissant les paires trouvées ou les objets découverts


#################    Affichage de tout le décor    #################


decor(td)


###############    Choix de la difficulté de jeu    ################


difficulte = textinput("Easy, Medium, Hard ?","Difficulté") # On demande la difficulté à l'utilisateur, pour définir le nombre de tentatives possibles.
while difficulte != "Easy" and difficulte != "Medium" and difficulte != "Hard":
    difficulte = textinput("Easy, Medium, Hard ?","Difficulté")
nb_tentatives = fonc_difficulte(difficulte)


##################    Boucle principale du jeu    #################


while (trouver != [True for i in range(len(case))]) : # tant que toutes les cases ne sont pas retournées et qu'il reste des tentatives, on continue, sinon on arrete et le jeu est terminé
    for i in trouver: 
        if i == False and (nb_tentatives > 0): 
            etape()

        elif nb_tentatives == 0 : # Si toutes les tentatives sont utilisées, alors la boucle s'arrête.
            rectangle(-750,-320,60,1700,tc,"white",0)
            texte("Nombre de tentatives atteintes, retentez votre chance !!!",0,-320,"green","Arial",52,tc)
            texte("0",642,295,"red","Arial",55,tc)


################    Affichage de fin de partie    #################

# Fin du jeu, toute les paires ont été trouvées
rectangle(-750,-320,62,1700,tc,"white",0)
texte("BIEN JOUÉ !!!",0,-320,"green","Arial",55,tc)
