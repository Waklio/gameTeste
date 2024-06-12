define gui.name_xpos = 347
define gui.dialogue_xpos = 347


define r = Character("Raisa", image = "raissa_empolgada")

image raisa_empolgada = "images/raisa_empolgada.png"
image raisa_animada = "images/raisa_animada.png"
image raisa_pensando = "images/raisa_pensando.png"
    


init python:
    def countdown():
        global timex
        if timex > 0:
            timex -= 1
        else:
            renpy.hide_screen("reassemble_puzzle")
            renpy.jump("again")

    import random

    def setup_puzzle():
        initial_piece_coordinates.clear()
        for i in range(page_pieces):
            start_x = 1100
            start_y = 133
            end_x = 1133
            end_y = 533
            rand_loc = (random.randint(start_x, end_x), random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc) 

    def piece_drop(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                
                renpy.jump("reassemble_complete")




label reassemble_complete:
    call screen show_complete_poster
    scene bg margem
    show raisa_animada at truecenter with moveintop
    r "Consegui!!! Ah menino, eu sou demais! Vou lá na biblioteca falar pra Fran e pra Raiana!
    Ó as coisas progredindo!! "
    r "Chama os créditos."
    return

screen reassemble_puzzle:
    add "background.png"

    frame:
        background "puzzle-frame.png"
        xysize full_page_size
        anchor (0.5, 0.5)
        pos (330, 200)

    draggroup:
        # Group of draggable pieces, and the spots they can be dragged.
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor (0.5, 0.5)
                focus_mask True
                drag_raise True
                image "Pieces/piece-%s.png" % (i + 1)

        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor (0.5, 0.5)
                focus_mask True
                image "Pieces/piece-%s.png" % (i + 1) alpha 0.0

   

screen show_complete_poster:
    modal True
    add "background.png"  
    vbox:
        xalign 0.5
        yalign 0.5
        add im.Scale("full-page.png", 500, 600)  
        textbutton "Seguir" action Return() align(0.5, 5.0)

default page_pieces = 12  
default full_page_size = (360, 360)
default piece_coordinates = [(249, 94), (429, 87), (533, 155), (231, 265), (392, 215), (416, 326), (482, 358), (250, 477), (463, 517), (258, 616), (451, 642), (570, 597)]
default initial_piece_coordinates = [] 
default finished_pieces = 0  


transform move_from_left_to_center:
    xalign 0.0
    linear 1.0 xalign 0.5 


