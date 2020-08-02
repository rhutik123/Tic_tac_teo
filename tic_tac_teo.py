# board
# play game
# check win
    # check row 
    # check column
    # check diagonal
# check tie
# handel turn
# flip player

# ---------global veriables

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

game_still_going = True

current_player = "X"

winner = None

def display_board():
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])

def paly_game():
    global winner
    global game_still_going
    display_board()

    while game_still_going:
        
        handel_turn(current_player)

        check_if_game_over()

        flip_turn()

    if winner == "X" or winner == "O":
        print(winner + " won !!!")
    else:
        print("Tie.")




def handel_turn(player):
    global current_player

    print(current_player + "'s turn.")

    position = input("Enter any position from 1-9 : ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Please enter position from 1-9 : ")
        
        position = int(position) - 1
        
        if board[position] == "-":
            valid = True
        else:
            print("can't go there")

    

    board[position] = current_player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
        return 

def check_rows():
    global game_still_going

    row1_win = board[0] == board[1] == board[2] != "-"
    row2_win = board[3] == board[4] == board[5] != "-"
    row3_win = board[6] == board[7] == board[8] != "-"

    if row1_win or row2_win or row3_win:
        game_still_going = False
    if row1_win:
        return board[0]
    if row2_win:
        return board[3]
    if row3_win:
        return board[6]


def check_columns():
    global game_still_going
    
    column1_win = board[0] == board[3] == board[6] != "-"
    column2_win = board[1] == board[4] == board[7] != "-"
    column3_win = board[2] == board[5] == board[8] != "-"

    if column1_win or column2_win or column3_win:
        game_still_going = False
    if column1_win:
        return board[0]
    if column2_win:
        return board[1]
    if column3_win:
        return board[2]


def check_diagonals():
    global game_still_going
    
    diagonal1_win = board[0] == board[4] == board[8] != "-"
    diagonal2_win = board[6] == board[4] == board[2] != "-"

    if diagonal1_win or diagonal2_win:
        game_still_going = False
    if diagonal1_win:
        return board[0]
    if diagonal2_win:
        return board[6]


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


def flip_turn():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

paly_game()







