import random as r
def makeBoard():
    tempboard = []
    for row in range(3):
        line = []
        for col in range(3):
            line.append(' ')
        tempboard.append(line)
    return tempboard

def printBoard(arg):
    count = 0
    for row in arg:

        for col in row:
            count += 1
            # if empty, then print the number
            if row[(count - 1) % 3] == " ":
                print(f"| {count} ", end="")
            else:
                print(f"| {row[(count - 1) % 3]} ", end="")

        if count % 3 == 0:
            print("|")
            print("-" * 13)


def getmove(argboard, player):
    while True:
        move = input("Choose your move ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9:
                move = move - 1
                row = move // 3
                col = move % 3

                if argboard[row][col] == " ":
                    argboard[row][col] = player
                    break
                else:
                    print(f"{move+1} is taken, dum dum")
            else:
                print("USE YOUR BRAIN")
        else:
            print("USE YOUR BRAIN")
    return argboard

def getplayer(player):
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player

def checkboard(argboard):
    win = [
        [argboard[0][0], argboard[0][1], argboard[0][2]], 
        [argboard[1][0], argboard[1][1], argboard[1][2]], 
        [argboard[2][0], argboard[2][1], argboard[2][2]], 

        [argboard[0][0], argboard[1][0], argboard[2][0]], 
        [argboard[0][1], argboard[1][1], argboard[2][1]], 
        [argboard[0][2], argboard[1][2], argboard[2][2]],

        [argboard[0][0], argboard[1][1], argboard[2][2]], 
        [argboard[0][2], argboard[1][1], argboard[2][0]] 
    ]

    for condition in win:
        if condition[0] == condition[1] == condition[2] and condition[0] != " ":
            return True
    return False

def checkDraw(argboard):
    for row in argboard:
        for col in row:
            if col == " ":
                return False
    return True

# 1. Check if AI can win in the next move == take that move.
# 2. Check if player can win in next move == block it.
# 3. If center is empty == take center.
# 4. If a corner is empty == take a corner.
# 5. Else == take any available space.

def aimove(board, cplayer):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = cplayer

                if checkboard(board):
                    return board
                else: 
                    board[i][j] = " "
    if cplayer == "X":
        opponent = "O"
    else:
        opponent = "X"
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = opponent

                if checkboard(board):
                    board[i][j] = current
                    return board
                else:
                    board[i][j] = " "
    if board[1][1] == " ":
        board[1][1] = cplayer
        return board
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
    corners = r.shuffle(corners)
    for i, j in r.shuffle(corners):
        if board[i][j] == " ":
            board[i][j] = cplayer
            return board
    
        



current = "none"
board = makeBoard()
while True:
    printBoard(board)
    current = getplayer(current)
    if current == "X":
        board = getmove(board, current)
    else:
        board = aimove(board, current)
    if checkboard(board):
        printBoard(board)
        print(f"Player {current} wins because they cheated!")
        break
    if checkDraw(board):
        printBoard(board)
        print("both of you suck")