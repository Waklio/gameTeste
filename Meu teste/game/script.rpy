# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define z = Character("zebê")
define d = Character("Dirda")
define n = ("narrador")

image solescaldante  = "images/solescaldante.png"
image Dirda = "images/Dirda.png"
image Zebê = "images/Zebê.png"



# The game starts here.

label start:

    scene solescaldante:
        zoom 1.88

    n  "Perdidas no deserto de solbral"

    show Dirda:
        zoom 0.5    
    
    d "Se continuar assim a gente morre de ensolação"

    show Zebê:
        zoom 0.5
           
    z "Poisé, então conserva as tuas forças e cale a boca"

    

     

    #This ends the game.

    return
