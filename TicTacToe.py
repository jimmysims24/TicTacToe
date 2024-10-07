def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board, player):
    win_conditions = [
        # Rows
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        # Columns
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        # Diagonals
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    return ' ' not in board

def tic_tac_toe():
    board = [' ' for i in range(9)]
    current_player = 'X'

    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (0-8): "))

        if board[move] == ' ':
            board[move] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell is already taken, choose another one.")

tic_tac_toe()
