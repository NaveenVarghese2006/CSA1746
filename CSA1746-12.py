# Simple Tic Tac Toe game with auto moves and output

def print_board(board):
    for row in board:
        print(' | '.join(row))
    print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]): return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2-i] == player for i in range(3)]): return True
    return False

def auto_tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    moves = [(0,0), (1,1), (0,1), (0,2), (2,2)]  # Predefined moves
    players = ['X', 'O'] * 5
    for move, player in zip(moves, players):
        row, col = move
        if board[row][col] == ' ':
            board[row][col] = player
            print_board(board)
            if check_winner(board, player):
                print(f"Player {player} wins!")
                return
    print("Draw!")
auto_tic_tac_toe()
