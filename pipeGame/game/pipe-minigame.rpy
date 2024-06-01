init python:
    def setup_pipe_game():
        global pipes
        global connected_pipes
        
        #reseta a lista pra vazia para poder receber novos canos.
        pipes = []
        connected_pipes = []

        #gera o ccaminho do inicio ao fim 
        generate_grid_path()

        create_pipes()

    def create_pipes():

        for i in range(1, amount_of_pipes + 1):
            # é verificado a próxima celula se estiver  a direita cano reto e se estiver abaixo cano curvo
            if i == 1:
                if grid_path[0] + 1 == grid_path[1]:
                    create_pipe(type="straight", cell = i)
                elif grid_path[0] + pipe_columns == grid_path[1]:
                    create_pipe(type="curved", cell = i)
            # verificações para determinar o tipo de cano apropriado 
            elif i > 1 and i < amount_of_pipes:

                if i in grid_path:
                    # calculo do inidicie atual 
                    current_cell_index = grid_path.index(i)
                    next_cell_index = current_cell_index + 1
                    prev_cell_index = current_cell_index - 1
                    #se estiver na borda esquerda, verifica se o proximo passo esta a direita ou abaixo
                    if grid_path[current_cell_index] % pipe_columns == 1:
                        if grid_path[current_cell_index] + 1 == grid_path[next_cell_index]:
                            create_pipe(type="curved", cell=grid_path[current_cell_index])

                        elif grid_path[current_cell_index] + pipe_columns == grid_path[next_cell_index]:
                            create_pipe(type="straight", cell = grid_path[current_cell_index])
                    #no topo cria cano curvo 
                    elif grid_path[current_cell_index] % pipe_columns == 0 and grid_path[current_cell_index] <= pipe_columns:
                        create_pipe(type="curved", cell=grid_path[current_cell_index])
                    # se estiver na borda direita, verifica se caminho vem de cima ou da esqueda  e cria cano adequado 
                    elif grid_path[current_cell_index] % pipe_columns == 0 and grid_path[current_cell_index] > pipe_columns:
                            # para outras posições verifica a direção e cria varias posiçoes  relativa a grid
                        if grid_path[current_cell_index] - pipe_columns == grid_path[prev_cell_index]:
                            create_pipe(type="straight", cell=grid_path[current_cell_index])

                        elif grid_path[current_cell_index] - 1 == grid_path[prev_cell_index]:
                            create_pipe(type="curved", cell = grid_path[current_cell_index])
                    else:
                        if grid_path[current_cell_index] <= pipe_rows:

                            if grid_path[current_cell_index] + 1 == grid_path[next_cell_index]:
                                create_pipe(type="straight", cell = grid_path[next_cell_index])

                            elif grid_path[current_cell_index] + pipe_columns == grid_path[next_cell_index]:
                                create_pipe(type="curved", cell=grid_path[current_cell_index])

                        elif grid_path[current_cell_index] >= amount_of_pipes - pipe_columns:

                            if grid_path[current_cell_index] - pipe_columns == grid_path[prev_cell_index]:
                                create_pipe(type="curved", cell = grid_path[current_cell_index])

                            elif grid_path[current_cell_index] - 1 == grid_path[prev_cell_index]:
                                create_pipe(type="straight", cell = grid_path[current_cell_index])
                        else:
                            if grid_path[current_cell_index] - 1 == grid_path[prev_cell_index]:

                                if grid_path[current_cell_index] + 1 == grid_path[next_cell_index]:
                                    create_pipe(type="straight", cell = grid_path[current_cell_index])

                                elif grid_path[current_cell_index] + pipe_columns == grid_path[next_cell_index]:
                                    create_pipe(type="curved", cell = grid_path[current_cell_index])

                            elif grid_path[current_cell_index] - pipe_columns == grid_path[prev_cell_index]:

                                if grid_path[current_cell_index] + 1 == grid_path[next_cell_index]:
                                    create_pipe(type="curved", cell = grid_path[current_cell_index])

                                elif grid_path[current_cell_index] + pipe_columns == grid_path[next_cell_index]:
                                    create_pipe(type="straight", cell = grid_path[current_cell_index])
                else:
                    random_type = renpy.random.choice(list(pipe_types.keys()))
                    create_pipe(type=random_type, cell=i)
                    #para ultima celula verifica a direção do passo anterior e determina se é reto ou curvo o cano
            elif i == amount_of_pipes:
                current_cell_index = grid_path.index(i)

                if grid_path[current_cell_index] - 1 == grid_path[-2]:
                    create_pipe(type="straight", cell = grid_path[current_cell_index])
                else:
                    create_pipe(type="curved", cell = grid_path[current_cell_index])

    def create_pipe(type, cell):
        pipe_image = f"{type}-pipe.png"
        pipe_end_points = list(pipe_types[type])
        final_pipe = [pipe_image, type, pipe_end_points, cell, 0]
        pipes.append(final_pipe)

    def generate_grid_path(): #gera apenas UM unico caminho do início ao fim, sempre escolhendo seguir pra ser direita ou pra baixo
        global grid_path

        grid_path = [1]

        for i in range(pipe_columns + pipe_rows - 2): # é escolhido as 7 celulas necessárias para finalizar o minigame

            # Aqui é testado  3 condições, esse primeiro if diz :se a celula atual está na ultima coluna  adiciona abaixo.
            if grid_path[-1] % pipe_columns == 0 and grid_path[-1] <= amount_of_pipes - pipe_columns:
                grid_path.append(grid_path[-1] + pipe_columns)

            # celula atual n esta na ultima colina e existe celulas abaixo, escolha mover aleatoriamente pra 
            # direita ou para baixo e adicionea proxima celula
            elif grid_path[-1] % pipe_columns != 0 and grid_path[-1] <= amount_of_pipes - pipe_columns:
                potential_cells = ["right", "down"]

                random_pick = renpy.random.choice(potential_cells)
                if random_pick == "right":
                    grid_path.append(grid_path[-1] + 1)

                elif random_pick == "down":
                    grid_path.append(grid_path[-1] + pipe_columns)

            #Se a célula atual nas últimas linhas e n existe células abaixo, mova para a direita
            elif grid_path[-1] > amount_of_pipes - pipe_columns:
                grid_path.append(grid_path[-1] + 1)

    def update_pipe_endpoints(cell):
        for pipe in pipes:

            if pipe[3] == cell:

                for endpoint in pipe[2]:
                    if endpoint == "top":
                        endpoint_index = pipe[2].index("top")
                        pipe[2][endpoint_index] = "right"
                    elif endpoint == "right":

                        endpoint_index = pipe[2].index("right")
                        pipe[2][endpoint_index] = "bottom"

                    elif endpoint == "bottom":
                        endpoint_index = pipe[2].index("bottom")
                        pipe[2][endpoint_index] = "left"

                    elif endpoint == "left":
                        endpoint_index = pipe[2].index("left")
                        pipe[2][endpoint_index] = "top"
                break

    def rotate_pipe(cell):

        if pipes[cell-1][4] == 360:
            pipes[cell-1][4] = 90

        else:
            pipes[cell-1][4] += 90

        update_pipe_endpoints(cell)

        check_pipe_connections()

    def check_pipe_connections():
        global connected_pipes

        connected_pipes = []

        if "left" in pipes[0][2] and pipes[0] not in connected_pipes:
            connected_pipes.append(pipes[0])

        if len(connected_pipes) > 0 and connected_pipes[0][3] == 1:

            for pipe in connected_pipes:
                pipe_to_add = None

                if pipe[3] % pipe_columns == 1 and pipe[3] != 1 and "left" in pipe[2]:
                    break

                if pipe[3] % pipe_columns != 0:

                    if "right" in pipe[2]:
                        if "left" in pipes[pipe[3]][2]:
                            if pipes[pipe[3]] not in connected_pipes:
                                pipe_to_add = pipes[pipe[3]]
                        else:
                            break

                if pipe[3] <= amount_of_pipes - pipe_columns:

                    if "bottom" in pipe[2]:
                        if "top" in pipes[pipe[3] - 1 + pipe_columns][2]:
                            if pipes[pipe[3] - 1 + pipe_columns] not in connected_pipes:
                                pipe_to_add = pipes[pipe[3] - 1 + pipe_columns]
                        else:
                            break

                elif pipe[3] > amount_of_pipes - pipe_columns and "bottom" in pipe[2]:
                    break

                if pipe[3] > pipe_columns:

                    if "top" in pipe[2]:

                        if "bottom" in pipes[pipe[3] - 1 - pipe_columns][2]:

                            if pipes[pipe[3] - 1 - pipe_columns] not in connected_pipes:
                                pipe_to_add = pipes[pipe[3] - 1 - pipe_columns]
                        else:
                            break

                elif pipe[3] <= pipe_columns and "top" in pipe[2]:
                    break

                if pipe[3] % pipe_columns != 1 and pipe[3] != amount_of_pipes:

                    if "left" in pipe[2]:

                        if "right" in pipes[pipe[3] - 2][2]:

                            if pipes[pipe[3] - 2] not in connected_pipes:
                                pipe_to_add = pipes[pipe[3] - 2]
                        else:
                            break

                if pipe_to_add is not None:
                    connected_pipes.append(pipe_to_add)

        if len(connected_pipes) > 0:

            if amount_of_pipes == connected_pipes[-1][3]:

                if "right" not in connected_pipes[-1][2]:
                    connected_pipes.pop(-1)
                else:
                    renpy.show_screen("pipe_game_success")

screen pipe_game_success:
    modal True
    frame:
        background "#00000080"
        xfill True
        yfill True
        frame:
            xsize 450
            ysize 200
            padding (20, 15)
            align(0.5, 0.5)
            text "Success! Play again?" color "#FFFFFF" size 30 align (0.5, 0.2)
            grid 2 1:
                spacing 100
                align (0.5, 0.9)
                textbutton "Yes" text_color "#FFFFFF" text_size 30 xalign 0.5 action [Function(setup_pipe_game), Hide("pipe_game_success")]
                textbutton "No" text_color "#FFFFFF" text_size 30 xalign 0.5 action Function(renpy.full_restart)

screen connect_the_pipes:

    image "background.png"

    grid pipe_columns pipe_rows:
        spacing 0
        pos (640, 140)
        anchor (0.0, 0.0)

        for pipe in pipes:

            if pipe in connected_pipes:
                imagebutton idle Transform(f"{pipe[1]}-pipe-connected.png", rotate = pipe[4], rotate_pad=False) action Function(rotate_pipe, cell = pipe[3])
            else:
                imagebutton idle Transform(pipe[0], rotate = pipe[4], rotate_pad = False) action Function(rotate_pipe, cell = pipe[3])

# Declaração das varáveis globais
default pipe_rows = 4  # numero de linhas 
default pipe_columns = 4 # numero de colunas
default amount_of_pipes = pipe_rows * pipe_columns # numero total de canos que estão no minigame
default grid_path = []  #Var responsavel pelounico caminho certo 
default pipes = [] # guarda os formatos de canos (t, reto, cruz)
default pipe_types = {"straight": ("top", "bottom"), "curved": ("right", "bottom"), "t": ("top", "bottom", "left"), "cross": ("bottom", "left", "top", "right")}
# pipe_types é um dicionario que guarda os canos bem como as suas extremidades
default connected_pipes = []
# rastreia a conexão do canos 

