import os
import random


# Define a function to clear the screen
def clear():
    os.system('cls')


# Define a function to display the board
def display_board(board):
    clear()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Define a function to get the player input from board
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O ?').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# Define a function to determine the position and assign it to the board
def place_marker(board, marker, position):
    board[position] = marker


# Define a function to check who is won
def win_check(board, mark):
    return (
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[7] == mark and board[4] == mark and board[1] == mark) or
        (board[8] == mark and board[5] == mark and board[2] == mark) or
        (board[9] == mark and board[6] == mark and board[3] == mark) or
        (board[7] == mark and board[5] == mark and board[3] == mark) or
        (board[9] == mark and board[5] == mark and board[1] == mark))


# Define which player go first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# Define a function to tell the free space on board
def check_space(board, position):
    return board[position] == ' '


# Define a function to find if the board is full
def full_board_check(board):
    for i in range(1,10):
        if check_space(board, i):
            return False
    return True


# Define the Player's choice and the check for free space
def player_choice(board):
    position = ' '
    while position not in '1,2,3,4,5,6,7,8,9'.split() or not check_space(board, int(position)):
        position = input("Choose your next position: (1-9)")
        return int(position)


# Define the function to ask a Player wants to play again
def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')


# Call all the functions
print("Lets Play Tic Tac Toe!!!")
while True:
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "Will go first")
    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulation !!! you have won the game")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is draw!!!!")
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Congratulation !!! you have won the game")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is tie!!!")
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break