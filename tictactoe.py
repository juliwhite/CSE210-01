"""
Name: Julieta White
Course: CSE 210
Brother: Nathan Parrish
Competency: Disign a Tic-Tac-Toe game.

"""


# The program must have a function called main.
# The function main(), primarily invite the user to play the game 
# while user say yes, the function proceed to call other functions. 
def main():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    play_game = True
    choice = input("Do you want to play tic tac toe game? (y/n): ")
    show_board(board)
    while play_game:
        if choice == "y" or choice == "Y":
            print("Let's play tic tac toe!")
            #show_board(board)
            ask_position(board)
            #show_board(board)

            if check_winner(board) or check_winner(board) == False:
                play_game = False
                break
        else:
            print("Thank you.")
            play_game = False
            break

# The function show_board() display the board for the user. 
def show_board(board):
    
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print("- + - + - ")
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print("- + - + - ")
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))

# The function ask_position ask the player for a position in the board.    
def ask_position(board):

    for i in range(9):
        if (i % 2) == 0:
            position = int(input("Entry position for x, from 1-9 : "))
            board[position - 1] = "x"
            show_board(board)
            if check_winner(board):
                print("\n")
                print("Player x won!")
                break
           
        elif (i % 2) != 0:
            position = int(input("Entry position for o, from 1-9 : "))
            board[position - 1] = "o"
            show_board(board)
            if check_winner(board):
                print("\n")
                print("Player o won!")
                break
    
    #show_board(board)
        
            
# the function check_winner() return True when a winner has been found.    
def check_winner(board):
    x = "x"
    o = "o"
    if board[0] == board[1] == board[2] == x or board[0] == board[1] == board[2] == o:
        return True
    elif board[3] == board[4] == board[5] == x or board[3] == board[4] == board[5] == o:
        return True
    elif board[6] == board[7] == board[8] == x or board[6] == board[7] == board[8] == o:
        return True
    elif board[0] == board[3] == board[6] == x or board[0] == board[3] == board[6] == o:
        return True
    elif board[1] == board[4] == board[7] == x or board[1] == board[4] == board[7] == o:
        return True
    elif board[2] == board[5] == board[8] == x or board[2] == board[5] == board[8] == o:
        return True
    elif board[0] == board[4] == board[8] == x or board[0] == board[4] == board[8] == o:
        return True
    elif board[2] == board[4] == board[6] == x or board[2] == board[4] == board[6] == o:
        return True
    else: 
        return False

if __name__ == "__main__":
    main()

