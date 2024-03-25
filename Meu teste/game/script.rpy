# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    Dirda = True

    

define z = Character("zebê")
define d = Character("Dirda")
define n = ("narrador")
define g = ("genius")

image solescaldante  = "images/solescaldante.png"
image Dirda = "images/Dirda.png"
image Zebê = "images/Zebê.png"
image ruina = "images/ruina1.png"
image magic = "images/magicLamp.png"
image genio = "images/genius.png"



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

    scene ruina:
        zoom 1.88

    show zebê at right:
        zoom 0.5
    z "o que é isso enterrado na areia ??"
    z "É uma lampâda mágica"
    scene ruina:
        zoom 1.88
    show magic at center:
        zoom 0.3

    show Dirda at left:
        zoom 0.5
    d "que sorte a nossa"
    hide Dirda
    hide Zebê

    n"A Dirda pega lampada e esfrega e então..."

    scene ruina:
        zoom 1.88
    show genio at center:
        zoom 0.5    
    play music"audio/risada.ogg"noloop

    show Dirda  at left:
        zoom 0.5

    show zebê at right:
        zoom 0.5
    g "Eu sou genivaldo o gênio, por me libertarem concendo a vocÊs 1 desejo pra cada uma ??"
    g "APENAS UM"

    n "Escolha o personagem que irá fazer o pedido primeiro"
     
    menu:
        "Dirda":
            $Dirda = True
            jump endGame
                
        "Zebê":
            $Dirda = False
            hide Dirda
            show Zebê at right:
                zoom 0.5
            z "Quero riquezas"
            g "Feito e vc Dirda"
            show Dirda at left: 
                zoom 0.5
            d "Quero ir pra casa"
            g " Feito"
    play music"audio/winner.ogg"
    n " BOM JOGO, Escolha certa"

    return


    label endGame:
    if Dirda == True:
        hide zebê
        d "Certo, vou primeiro"
        d "Quero voltar pra casa"
        hide Dirda
        n "Dirda desaparece e volta pra casa"
    g "Feito"

    g "E você Zebê?"

    show zebê at right:
        zoom 0.5
        
        
    z "Traga ela de volta"
    g "Feito"
        
    show Dirda at left:
        zoom 0.5
    play music"audio/lose.ogg"
    n " Fim do jogo, vc perdeu."
    

  



    

     

    #This ends the game.

    return
