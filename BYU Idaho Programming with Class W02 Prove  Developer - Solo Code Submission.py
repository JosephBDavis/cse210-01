# Tic Tac Toe Week 2 Prove Assignments



def main():
    player = next_player("")
    board = create_board()
    while not (winner(board) or draw(board)):
        display_board(board)
        move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for box in range(9):
        board.append(box + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def draw(board):
    for box in range(9):
        if board[box] != "O"and board[box] !="X":
            return False
    return True


def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[1] == board[2] == board[3] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[3] == board[5] == board[7] or
            board[3] == board[6] == board[9] or
            board[4] == board[5] == board[6])


def move(player, board):
    box = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[box - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return 'o'

if __name__ == "__main__":
    main()