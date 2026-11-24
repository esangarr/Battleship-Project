#Prueba commit nati
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

    otras cosas
    - si escribe mal las coordenadas (con un espacio en lugar de coma o letras)
    - si encima los barcos
    - el 10 en el tablero desacomodando la fila

"""

def create_board():
    board = ["  1 2 3 4 5 6 7 8 9 10"]
    for i in range(1,10+1):
        board.append(f"{i} - - - - - - - - - -")
    return board

print(f"⋆༺𓆩☠︎︎𓆪༻⋆¡Bienvenido a la Batalla Naval!⋆༺𓆩☠︎︎𓆪༻⋆\n ")

def loading():
    print("Cargando ҉")
    for l in range(0,2):
        print("*\n~")


def print_board(board):
    loading()
    print("El tablero se generó exitosamente")
    for i in board:
        print(i)

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
                   
    return valid

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

    return boat

def create_user_boat(board):
    print(f"Coloca tus barcos en el tablero ☸")
    player_board = board

    boats = []

    size = 2
    for i in range(1,3+1):
        print_board(player_board)
        print(f"\n--------------- Creando barco {i} ---------------")
        
        boat = get_user_boat(size)

        for j in range(0, len(boat), 2):
            row = boat[j]
            column = boat[j+1]
            
            elementos_fila = player_board[row].split(" ")
            
            elementos_fila[column] = "B"
            
            player_board[row] = " ".join(elementos_fila)

        boats.append(boat)
        print(f"\n--------------- Barco {i} Creado  𓊝  Tamaño: {size}---------------")
        print_board(player_board)
        print("\n")
        size += 1


    print(boats)

def main(args=0):
    create_user_boat(create_board())

if __name__ == "__main__":
    main()