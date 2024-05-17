def multiplayer(board):
    print("Player 1: X")
    print("Player 2: O")
    for i in range(9): 
        if i % 2 == 0:
            while True:
                try:
                    position = int(input("Player 1 Enter the position (1 - 9): "))
                    if 1 <= position <= 9 and board[position - 1] == 0:
                        board[position - 1] = 1
                        break
                    else:
                        print("Wrong input!!! TRY AGAIN")
                except KeyboardInterrupt:
                    print("\nGame interrupted. Exiting...")
                    return
        else:
            while True:
                try:
                    position = int(input("Player 2 Enter the position (1 - 9): "))
                    if 1 <= position <= 9 and board[position - 1] == 0:
                        board[position - 1] = -1  
                        break
                    else:
                        print("Wrong input!!! TRY AGAIN")
                except KeyboardInterrupt:
                    print("\nGame interrupted. Exiting...")
                    return
        current_board(board)
        winner = analyse_board(board)
        if winner:
            if winner == 1:
                print("PLAYER 1 HAS WON")
            else:
                print("PLAYER 2 HAS WON")
            return
    print("DRAW")

def current_board(board):
    new_board = []
    for i in range(len(board)):
        if board[i] == 0:
            new_board.append("_") 
        elif board[i] == 1:
            new_board.append("X")
        elif board[i] == -1:
            new_board.append("O")

    for i in range(0, 9, 3):  # Ensure correct boundaries
        print(new_board[i], "\t", new_board[i + 1], "\t", new_board[i + 2], "\n")

def analyse_board(board):
    for i in range(0,7,3):
        if board[i] == board[i+1] and board[i+1] == board[i+2] and board[i] != 0:
            return board[i]
    for i in range(3):
        if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] != 0:
            return board[i]
    if board[0] == board[4] == board[8] and board[0] != 0:
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != 0:
        return board[2]
    return 0  # Return 0 if there is no winner




board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Multiplayer game: \n")
multiplayer(board)
