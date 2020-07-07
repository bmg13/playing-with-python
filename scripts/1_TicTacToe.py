from board import view_board

import random

class Game:

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'



def player_input():
    value = ""
    
    while value != "x" and value != "o":
        value = input("Player 1, choose 'x' or 'o': ").lower()
    
    player1 = value
    if player1=="x":
        player2="o"
    else:
        player2="x"

    return (player1, player2)


def place_value(board, value, position):
    board[position] = value


def confirm_win(board, mark):
    '''
    board:
    7 - 8 - 9
    4 - 5 - 6
    1 - 2 - 3
    '''
    
    # check rows
    if(board[1] == board[2] == board[3] == mark):
        return True
    if(board[4] == board[5] == board[6] == mark):
        return True
    if(board[7] == board[8] == board[9] == mark):
        return True
    # check columns
    if(board[1] == board[4] == board[7] == mark):
        return True
    if(board[2] == board[5] == board[8] == mark):
        return True
    if(board[3] == board[6] == board[9] == mark):
        return True
    # check diagonals
    if(board[1] == board[5] == board[9] == mark):
        return True
    if(board[3] == board[5] == board[7] == mark):
        return True
    
    return False


def check_space_availability(board, position):
    # Check availability of a slot in the board
    return board[position] == " "


def check_if_board_is_full(board):
    for i in range(1,10):
        if check_space_availability(board, i):
            return False
    return True



def value_chosen(board):
    choice = 0
    acceptable_range = range(1,10)
    is_in_range = False
    while is_in_range == False or not check_space_availability(board, choice):
        choice = int(input("Please enter a position (1 to 9): "))
        # garantee that the input is within the defined range
        if(int(choice) not in acceptable_range):
            print("Incorrect value. Choice is not within the defined range.")
        else:
            is_in_range = True
    return choice



def continue_playing():
    choice = "Incorrect value"
    acceptable_range = ["Y", "N"]
    keep_playing = False
    while choice not in acceptable_range:
        choice = input("Continue playing? (Y or N) ")
        # garantee that the input is of a valid type
        if(choice not in acceptable_range):
            print("Incorrect value. Choice is not Y or N.")
    
    if(choice == "Y"):
        keep_playing = True
        
    return keep_playing



def play_tic_tac_toe():
    game_on = True
    test_board = [" "]*10
    player1_mark,player2_mark = player_input()
    turn = choose_first()
    
    while game_on:
        if turn == "Player 1":
            # view board
            view_board(test_board)
            # mark position
            position = value_chosen(test_board)
            # place value
            place_value(test_board,player1_mark,position)
            # check victory
            if(confirm_win(test_board,player1_mark)):
                view_board(test_board)
                print("Player 1 wins!")
                game_on = False
            else:
                # check if board is full (a tie)
                if(check_if_board_is_full(test_board)):
                    view_board()
                    print("TIE...")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            # view board
            view_board(test_board)
            # mark position
            position = value_chosen(test_board)
            # place value
            place_value(test_board,player2_mark,position)
            # check victory
            if(confirm_win(test_board,player2_mark)):
                view_board(test_board)
                print("Player 2 wins!")
                game_on = False
            else:
                # check if board is full (a tie)
                if(check_if_board_is_full(test_board)):
                    view_board(test_board)
                    print("TIE...")
                    game_on = False
                else:
                    turn = "Player 1"
        
        if(game_on):
            game_on = continue_playing()