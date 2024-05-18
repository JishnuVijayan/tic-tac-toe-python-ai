def single_player(board):
    print("Computer: X")
    print("Player: O")
    print("Do you want to play first or second?")
    c = int(input("Enter 1 for playing first and 2 for playing second: "))
    for i in range(9):
        if (i + c) % 2 == 0:
            new_computer_board = computer_turn(board)
            current_board(new_computer_board)
            winner = analyse_board(new_computer_board)
            if winner:
                if winner == 1:
                    print("COMPUTER HAS WON")
                return
        else:
            new_player_board = player_turn(board)
            current_board(new_player_board)
            winner = analyse_board(new_player_board)
            if winner:
                if winner == -1:
                    print("PLAYER HAS WON")
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

def player_turn(board):
    while True:
        try:
            position = int(input("Player 1 Enter the position (1 - 9): "))
            if 1 <= position <= 9 and board[position - 1] == 0:
                board[position - 1] = -1
                break
            else:
                print("Wrong input!!! TRY AGAIN")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            return
    return board

def is_win(board, letter):
    for i in range(0,7,3):
        if board[i] == board[i+1] and board[i+1] == board[i+2] and board[i] == letter:
            return True
    for i in range(3):
        if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] == letter:
            return True
    if board[0] == board[4] == board[8] and board[0] == letter:
        return True
    if board[2] == board[4] == board[6] and board[2] == letter:
        return True
    return False

def is_draw(board):
    return all(x != 0 for x in board)

def minimax(board, is_maximizing):
    computer_symbol = 1
    player_symbol = -1
    
    if is_win(board, computer_symbol):
        return 1 
    if is_win(board, player_symbol):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing: 
        best_score = -float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = computer_symbol
                score = minimax(board, False)
                board[i] = 0
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = player_symbol
                score = minimax(board, True)
                board[i] = 0
                best_score = min(best_score, score)
        return best_score

def computer_turn(board):
    print("Computer turn")
    best_score = -float('inf')
    best_pos = 0
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = minimax(board, False)
            board[i] = 0
            if score > best_score:
                best_score = score
                best_pos = i 
    board[best_pos] = 1
    return board
            

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Singleplayer game: \n")
single_player(board)
