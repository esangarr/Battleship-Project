import random as rd

"""Objetivos de hoy
    - Comentarios para funciones

    Completado
    - Y se pueden agregar botes al tablero
    -  Filtro de colisiones entre barcos (Si se colocan dos barcos en un mismo lugar)

    
    Faltante
    - Prints cada que haceer algo (mejora experiencia)
    - Comentarios en las fucnines describiendo su funcion
    - Comentarios más especificos
    - Filtro de fomato para coordenadas x,y

    otras cosas
    - si escribe mal las coordenadas (con un espacio en lugar de coma o letras)
    - si encima los barcos
    - el 10 en el tablero desacomodando la fila

"""

def create_board():
    board = ["  1 2 3 4 5 6 7 8 9 10"]
    for i in range(1,10+1):
        board.append(f"{i} ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    return board

def loading():
    print("Cargando ҉")
    for l in range(0,2):
        print("*\n~")

def boat_to_board(boat, board):
    for j in range(0, len(boat), 2):
        row = boat[j]
        column = boat[j+1]
                
        elementos_fila = board[row].split(" ")
                
        elementos_fila[column] = "B"
                
        board[row] = " ".join(elementos_fila)

def print_board(board):
    loading()
    for i in range(0, len(board)):
        if i < 10:
            print(" " + board[i]) # Agrega un espacio visual a las filas 1-9
        else:
            print(board[i])
    print(f"\n-------- El tablero se generó exitosamente --------")

def valid_direction(boat, direction):
    match direction:
            case "h":
                h_list = []
                for e in range(0, len(boat), 2):
                    h_list.append(boat[e])
    
                right_e = h_list[0]
                for j in h_list:
                    if right_e != j:
                        valid = False
                    else:
                        valid = True
    
            case "v":
                v_list = []
                for e in range(1, len(boat), 2):
                    v_list.append(boat[e])
        
                right_e = v_list[1]
                for j in v_list:
                    if right_e != j:
                        valid = False
                    else:
                        valid = True

            case _:
                h_list = []
                for e in range(0, len(boat), 2):
                    h_list.append(boat[e])
                    
                right_e = h_list[0]
                for j in h_list:
                    if right_e != j:
                        valid = False
                    else:
                        valid = True
                   
    return valid

def valid_continuity(boat, direction):
    valid = True
    match direction:
        case "h":
            h_list = []
            for e in range(1, len(boat), 2):
                h_list.append(boat[e])

            x = h_list[0]

            for e in h_list:
                if x != e:
                    valid = False
                else:
                    valid = True
                
                x = x + 1 

        case "v":
            v_list = []
            for e in range(0, len(boat), 2):
                v_list.append(boat[e])
            
            x = v_list[0]
            for e in v_list:
                if x != e:
                    valid = False
                else:
                    valid = True
                            
                x = x + 1 

    return valid

def valid_boat(boat):

    if boat == []:
        return False

    states = []
    valid = True
    
    for c in boat:
        if c > 10:
            states.append(False)
        else:
            states.append(True)

    if False in states:
        valid = False
    else:
        valid = True


    return valid

def clean_coordinates(coordinate):
    c_string = coordinate.strip()
    c_string = coordinate.split(",")
    c_int = [int(c_string[0]), int(c_string[1])]

    return c_int

def input_coordinates(boat, size):
    print("\nIngresa las coordenadas del tablero donde quieres colocar tu barco. Ingrésalas como x,y (ejemplo: 1,2)")
    
    for i in range(1, size+1):                   
        xy =  input(f"\nTus coordenadas x,y en el punto {i}: ")
        xy = clean_coordinates(xy)
        boat.append(xy[1])
        boat.append(xy[0])

def filter_direction(boat, size, direction):
    match direction.lower():
        case "h":
            input_coordinates(boat, size)
            if boat[0] != boat[2]:
                for i in range(0, len(boat), 2):
                    boat[i], boat[i+1] = boat[i+1], boat[i]

        case "v":
            input_coordinates(boat, size)
            if boat[1] != boat[3]:
                for i in range(0, len(boat), 2):
                    boat[i], boat[i+1] = boat[i+1], boat[i]

        case _:
            print("No se selecciono direccion valida - Usando dirección predeterminada (Horizontal)")
            input_coordinates(boat, size)
            if boat[0] != boat[2]:
                for i in range(0, len(boat), 2):
                    boat[i], boat[i+1] = boat[i+1], boat[i]

    return boat

def get_user_boat(size):
    
    direction = input("\n¿En qué dirección irá tu bote, vertical u horizontal? (v-h): ")

    boat = []

    boat = filter_direction(boat, size, direction)

    while valid_boat(boat) == False :
        boat = []
        print("El barco se sale del tablero. Vuelve a revisar tus coordenadas y coloca otro barco.")
        boat = filter_direction(boat, size, direction)
        valid_boat(boat)

    while valid_direction(boat, direction) == False:
        boat = []
        print("El barco no sigue una trayetoria recta. Vuelve a revisar tus coordenadas y coloca otro barco.")
        boat = filter_direction(boat, size, direction)
        valid_direction(boat, direction)

    while valid_continuity(boat, direction) == False:
        boat = []
        print("El barco no es continuo. Vuelve a revisar tus coordenadas y coloca otro barco.")
        boat = filter_direction(boat, size, direction)
        valid_continuity(boat, direction)
        
    return boat

def generate_random_boat(size):
    d_int = rd.randint(1,2)
    
    direction = " "
    match d_int:
        case 1:
            direction = "h"
        case 2:
            direction = "v"

    boat = [rd.randint(1,10), rd.randint(1,10)]
    for i in range(1, size):

        match direction:
            case "h":
                boat.append(boat[0])
                boat.append(boat[1]+i)

            case "v":
                boat.append(boat[0]+i)
                boat.append(boat[1])

    return boat

def random_boat_filtered(size):
    
    boat = []

    boat = generate_random_boat(size)
    
    while valid_boat(boat) == False :
        boat = []
        print("El barco generado se sale del tablero...")
        print("Generando nuevo barco")
        boat = generate_random_boat(size)
        valid_boat(boat)

    return boat
 
def avoid_colitions(boat, boats):
    
    boat_coord = []
    for i in range(0, len(boat), 2):
        boat_coord.append((boat[i], boat[i+1]))

    for b in boats:
        for i in range(0, len(b), 2):
            par_existente = (b[i], b[i+1])
            
            if par_existente in boat_coord:
                return True
                
    return False

def create_bot_boats():
    bot_board = create_board()
    boats = []

    print_board(bot_board)

    size = 2
    for _ in range(1,3+1):

        while True:
            boat = random_boat_filtered(size)
            print(boat)
            if avoid_colitions(boat, boats):
                print("¡Error! Ese barco choca con otro. Intenta en otra posición.")
            else:
                break

        boat_to_board(boat, bot_board)

        boats.append(boat)
        print_board(bot_board)

        size += 1

    print(boats)
    return bot_board


def create_user_board():
    player_board = create_board()
    boats = []
    print_board(player_board)
    print(f"\nColoca tus barcos en el tablero ☸")

    size = 2
    for i in range(1,3+1):
        print(f"\n--------------- Creando barco {i} ---------------")

        while True:
            boat = get_user_boat(size)
            if avoid_colitions(boat, boats):
                print("¡Error! Ese barco choca con otro. Intenta en otra posición.")
            else:
                break

        boat_to_board(boat, player_board)

        boats.append(boat)
        print(f"\n--------------- Barco {i} Creado  𓊝  Tamaño: {size}---------------")
        print_board(player_board)
        print("\n")
        size += 1

    print(boats)
    return player_board

def main(args=0):
    print(f"⋆༺𓆩☠︎︎𓆪༻⋆¡Bienvenido a la Batalla Naval!⋆༺𓆩☠︎︎𓆪༻⋆\n ")
    #create_user_board()
    create_bot_boats()

if __name__ == "__main__":
    main()