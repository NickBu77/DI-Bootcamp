# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.

board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ]
display=''


def display_board(board=board):
    print(' '*4+'TIC TAC TOE'+' '*4)
    print('*'*19)
    print('*  '+board[0][0]+'  |  '+board[0][1]+'  |  '+board[0][2]+'  *')
    print('*'+'-'*5+'|'+'-'*5+'|'+'-'*5+'*')    
    print('*  '+board[1][0]+'  |  '+board[1][1]+'  |  '+board[1][2]+'  *')
    print('*'+'-'*5+'|'+'-'*5+'|'+'-'*5+'*')   
    print('*  '+board[2][0]+'  |  '+board[2][1]+'  |  '+board[2][2]+'  *')
    print('*'*19)



def player_input(current_player):
    if current_player.upper() == 'X':
        print('Player_X, your turn.')
        row = int(input('Enter the row number (1, 2, or 3): '))
        col = int(input('Enter the column number (1, 2, or 3): '))
        board[row-1][col-1] = 'X'
    elif current_player.upper() == 'O':
        print('Player_O, your turn') 
        row = int(input('Enter the row number (1, 2, or 3): '))
        col = int(input('Enter the column number (1, 2, or 3): '))      
        board[row-1][col-1] = 'O'  

    return display_board(board)



def check_win(board):
    result = 'Continue'
    if (board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X') or (board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X') or (board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X') or (board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X') or (board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X') or (board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X') or (board[0][0]=='O' and board[1][0]=='O' and board[2][0]=='O') or (board[0][1]=='O' and board[1][1]=='O' and board[2][1]=='O') or (board[0][2]=='O' and board[1][2]=='O' and board[2][2]=='O') or (board[0][0]=='O' and board[0][1]=='O' and board[0][2]=='O') or (board[1][0]=='O' and board[1][1]=='O' and board[1][2]=='O') or (board[2][0]=='O' and board[2][1]=='O' and board[2][2]=='O'):
        result = 'Win'
    elif (board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' '):
        result = 'Tie'
    else:
        result = 'Continue'
    return result


def play(current_player):
    while True:
        player_input(current_player)
        result = check_win(board)
        if result == 'Win':
            print(f'Congrats, {current_player.upper()} wins!')
            break
        elif result == 'Tie':
            print('You both fail.')
            break
        elif result == 'Continue':
            if current_player.upper() == 'X':
                current_player = 'O'
            elif current_player.upper() == 'O':
                current_player = 'X'

current_player = input('Which player will begin, "X" or "O"?: ')
play(current_player)


