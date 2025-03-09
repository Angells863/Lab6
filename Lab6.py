#Lab 6 - Connect 4

def initialize_board(num_rows, num_cols): #Initialize Board
    board = []
    for i in range(num_rows):
        slash = ['-'] * num_cols
        board.append(slash)
    return board

def print_board(board): #Print Board
    for i in range(len(board)-1,-1,-1):
        slash_string = ""
        for cell in board[i]:
            slash_string += cell+" "
        print(slash_string[:-1])
    print()

def insert_chip(board, col, chip_type): #Insert Chip
    for slash in range(len(board)):
        if board[slash][col]=="-":
            board[slash][col]=chip_type
            return slash
    return -1

def check_if_winner(board, col, row, chip_type):
    num_rows = len(board)
    num_cols = len(board[0])
    count=0
    for i in range(num_rows):
        if board[i][col]==chip_type:
            count+=1
            if count==4:
                return True
        else:
            count=0

    count=0
    for i in range(num_cols):
        if board[row][i]==chip_type:
            count+=1
            if count==4:
                return True
        else:
            count=0
    return False

def game(): #Connect 4 Game
    columns = int(input("What would you like the height of the board to be?: "))
    rows = int(input("What would you like the length of the board to be?: "))
    board = initialize_board(columns, rows)
    print_board(board)
    player_chip=["x", "o"]
    turn=0
    total_moves=0
    moves=columns*rows

    while total_moves<moves:
        print(f"Player {turn+1}: Which column would you like to choose?")
        col=int(input())

        while col<0 or col>=columns:
            print("Invalid column. Please try again.")
            col=int(input())

        row = insert_chip(board, col, player_chip[turn])

        if row==-1:
            print("Column full. Please choose a different column")
            continue
        print_board(board)

        if check_if_winner(board, col, row, player_chip[turn]):
            print(f"Player 1 won the game!")
            return

        turn=1-turn
        total_moves+=1
    print("Draw. Nobody wins.")

if __name__ == "__main__":
    game()