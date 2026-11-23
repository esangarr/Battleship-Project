import random as rd

bot_board = []
reference_board = []

"""Objetivos de hoy
    - Lograr crear tablero de jugador
    - Comentarios para funciones
    - Print entre cada proceso
    - Depurar errores que pueda cometer el usuario

    Completado
    - Y se pueden agregar botes al tablero

    Por Decidir (Con mi nati)
    - Por ahora genera solo dos botes (se puede cambiar en el for linea 90) no se ha decidido la cantidad
    - No se si meter el filtro de direcciones
    - Hay muchos erroere suq epuede cometer el usuario que se pueden depurar
    
    Faltante
    - Prints cada que haceer algo (mejora experiencia)
    - Comentarios en las fucnines describiendo su funcion
    - Comentarios más especificos
    -  Filtro de colisiones entre barcos (Si se colocan dos barcos en un mismo lugar)
"""

def create_board():
    board = ["  1 2 3 4 5 6 7 8 9 10"]
    for i in range(1,10+1):
        board.append(f"{i} - - - - - - - - - -")
    return board

def print_board(board):
    for i in board:
        print(i)

def valid_boat(boat):

    if boat == []:
        return False

    valid = True
    for c in boat:
        if c > 10:
            valid = False
        else:
            valid = True
    return valid

def clean_cordinates(cordinate):
    c_string = cordinate.strip()
    c_string = cordinate.split(",")
    c_int = [int(c_string[0]), int(c_string[1])]

    return c_int

def input_cordinates(boat, size, i1,i2):
    for i in range(1, size+1):                   
        xy =  input(f"\nCordenada x,y punto {i} : ")
        xy = clean_cordinates(xy)
        boat.append(xy[i1])
        boat.append(xy[i2])

def register_boat(boat, size, direction):
    #Hacer filtro para que no importa como registre el usuario el bote 
    #si ya dijo que era horizontal o verticcal se mantenga asi

    #Aun no esta hecho por eso se veredundante el match
    match direction.lower():
        case "h":
            input_cordinates(boat, size)

        case "v":
            input_cordinates(boat, size)


    return boat
    
def get_user_boat():
    size = int(input("\nIngrese el tamaño de su bote: "))
    direction = input("\nIngrese la direccion del bote (v-h): ")

    boat = []

    boat = register_boat(boat, size, direction)

    while valid_boat(boat) == False:
        print("El barco se sale del tablero, por favor cloca totrio barco.")
        boat = register_boat(boat, size)

    print(boat)
    return boat

def create_user_boad(board):
    player_board = board

    boats = []

    for i in range(1,2+1):
        print_board(player_board)
        print(f"\n--------------- Creando barco {i} ---------------")
        boat = get_user_boat()

        for j in range(0, len(boat), 2):
            row = boat[j]
            column = boat[j+1]
            
            elementos_fila = player_board[row].split(" ")
            
            elementos_fila[column] = "B"
            
            player_board[row] = " ".join(elementos_fila)

        boats.append(boat)
        print(f"\n--------------- Barco {i} Creado ---------------")
        print_board(player_board)


    print(boats)

def main(args=0):
    create_user_boad(create_board())

if __name__ == "__main__":
    main()