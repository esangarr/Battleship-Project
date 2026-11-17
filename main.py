import random as rd

bot_board = []
player_board = []
reference_board = []

def create_board():
    board = ["  1 2 3 4 5 6 7 8 9 10"]
    for i in range(1,10+1):
        board.append(f"{i} - - - - - - - - - -")
    return board

def print_board(board):
    for i in board:
        print(i)

def create_botBoard():
    bot_board = create_board()

    size = 2
    for _ in range(3):
        boat = []
        
        d = 2 #rd.randint(1,2)
        match d:
            case 1: # Caso de que sea barcco vertical
                pass
            case 2: # Caso de que sea barco horizontal
                boat = [rd.randint(1,10),rd.randint(1,10)]

                for i in range(1,size):
                    if boat[1] == 10:
                        boat.append(boat[0])
                        boat.append(boat[1]-i)
                    else:
                        boat.append(boat[0])
                        boat.append(boat[1]-i)

        print(boat)

        size = size + 1

            


def main(args=0):
    create_botBoard()

if __name__ == "__main__":
    main()