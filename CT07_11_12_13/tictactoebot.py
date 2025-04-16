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
        if condition[0] == condition[1] == condition[2] and condition[0] == current:
            return True
    return False

def checkDraw(argboard):
    for row in argboard:
        for col in row:
            if col == " ":
                return False
    return True



current = "none"
board = makeBoard()
while True:
    printBoard(board)
    current = getplayer(current)

    if current == "X":
        board = getmove(board)


    board = getmove(board, current)
    if checkboard(board):
        printBoard(board)
        print(f"Player {current} wins because they cheated!")
        break
    if checkDraw(board):
        printBoard(board)
        print("both of you suck")