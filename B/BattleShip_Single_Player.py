#Legend
#X for placing ships and hits battleship
# '  ' for available
#'-' for  missed shot

from random import randint

HIDDEN_BOARD = [[''] * 8 for x in range(8)]
GUESS_BOARD = [[''] * 8 for x in range(8)]

letter_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

def print_board(board):
    print('   A  B  C  D  E  F  G  H  ')
    print(' -+-+-+-+-+-+-+-+-+-+-+-+-')
    row_number = 1
    for row in board:
        print("%d | %s|" % (row_number, " | ".join(row)))
        row_number += 1  #for increment

def create_ships(board):
    for ship in  range(5):
        ship_row, ship_column = randint(0,7) , randint(0,7)
        while HIDDEN_BOARD[ship_row][ship_column] =='X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'



def get_ship_location():
    row = input("please enter a ship row 1-8 : ")
    while row not in '12345678':
        print("please enter a valid row!")
        row = input("please enter a ship row 1-8 : ")
    column = input("please enter a ship column A-H : ").upper()
    while column not in 'ABCDEFGH':
        print("please enter a valid ship column!")
        column = input("please enter a ship column A-H : ").upper()
    return int(row) -1, letter_to_numbers[column]


def count_hit_ships( board):
    count =0
    for row in board:
        for column in row:
            if column =='X':
                count +=1
    return count


create_ships(HIDDEN_BOARD)
print_board(HIDDEN_BOARD)
turns =10
# print_board(HIDDEN_BOARD)
# print_board(GUESS_BOARD)
while turns > 0:
    print("Welcome to Battleship")
    print_board(GUESS_BOARD)
    row, colum = get_ship_location()
    if GUESS_BOARD [row] [colum] =='-':
        print("You already guessed that")
    elif HIDDEN_BOARD[row][colum] =='X':
        print("Congratulations, you have hit the battleship")
        GUESS_BOARD[row][colum] = 'X'
        turns -= 1
    else:
        print("Sorry, you missed")
        GUESS_BOARD[row][colum] ='_'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print("Congratulations, you have sunk all the battleships")
        break
    print("You have " + str(turns) + ' turns remaining')
    if turns==0:
        print("You ran out of turns !\nGame Over ")
        break
        
