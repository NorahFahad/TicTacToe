# -------- the global variables --------

#create The board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#if the game stil going
game_still_going = True
winner = None
current_player = "X"

#def for display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    #display the board
    display_board()

    #loop while the game is still going
    while game_still_going:
        #Handle a single turn of each player
        handle_turn(current_player)

        #Check if the game has ended
        check_if_game_over()

        #Flip to the other player
        flip_player()


        #The game has endeed
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

#def to Handle a single turn of each player
def  handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        #loop to check the input is in range from 1 to 9
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        #if to check the position is empty or not
        if board[position] == "-":
            valid = True
        else:
            print("You can't put here. Try again.")

    board[position] = player
    display_board()

#def to Check if the game has ended
def check_if_game_over():
    check_for_winner()
    check_if_tie()

#def to check if there is player won
def check_for_winner():
    global winner #to access the global variable
    #check rows
    row_winner = check_rows()
    #check columns
    columns_winner = check_columns()
    #check diagonals
    digonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif digonals_winner:
        winner = digonals_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going #to access the global variable
    #check if any row have the same value and not empty
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    # if any row match then stop the game
    if row1 or row2 or row3:
        game_still_going = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():
    global game_still_going #to access the global variable
    #check if any column have the same value and not empty
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    # if any column match then stop the game
    if column1 or column2 or column3:
        game_still_going = False

    #if to return the winner
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def check_diagonals():
    global game_still_going #to access the global variable
    #check if any diagonal have the same value and not empty
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    # if any diagonal match then stop the game
    if diagonal1 or diagonal2:
        game_still_going = False

    #if to return the winner
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return

#def to check if no one win
def check_if_tie():
    global game_still_going #to access the global variable
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player #to access the global variable
    #if the current player is X change it to O
    if current_player == "X":
        current_player = "O"
    #if the current player is O change it to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()