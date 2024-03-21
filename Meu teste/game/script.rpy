# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define z = Character("zebê")
define d = Character("Dirda")
define n = ("narrador")

image solescaldante  = "images/solescaldante.png"
image Dirda = "images/Dirda.png"
image Zebê = "images/Zebê.png"
image ruina = "images/ruina1.png"



# The game starts here.

label start:
    play music "audio/windsound.ogg"
    scene solescaldante:
        zoom 1.88
    with pixellate
    n  "Perdidas no deserto de solbral"

    show Dirda:
        zoom 0.5
    with dissolve    
    
    d "Se continuar assim a gente morre de ensolação"

    hide Dirda  
    with fade

    show Zebê at right:
        zoom 0.5
        yalign 0.7
    with dissolve       
    z "Poisé, então conserva as tuas forças e cale a boca"

    stop music

    scene solescaldante:
        zoom 1.88
    with fade
    n "Pouco tempo de depois"

    hide solescaldante

    play music "audio/taram.ogg" noloop

    scene ruina:
        zoom 1.88
    with dissolve
    n "E quando elas iriam de arrasta pra cima, surgiu..."

    show Dirda at left:
        zoom 0.5
    d "É uma ruina ??? Estamos á salvo"
    
    show Zebê at right:
        zoom 0.5
    z "Podemos finalmente descansar"

    



    

     

    #This ends the game.

    return
