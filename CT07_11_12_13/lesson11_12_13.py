# import random as r
# def diceGuess(guess):
#     if r.randint(1, 6) == guess:
#         return True
#     else:
#         return False
# if diceGuess(int(input("Guess a number "))):
#     print("Correct")
# else:
#     print("YOU ARE WRONG, GO BACK TO SCHOOL")



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
    board = getmove(board, current)
    if checkboard(board):
        printBoard(board)
        print(f"Player {current} wins because they cheated!")
        break
    if checkDraw(board):
        printBoard(board)
        print("both of you suck")
        break
# winner = ""

# board = [
#     "1", "2", "3", 
#     "4", "5", "6", 
#     "7", "8", "9"
# ]
# conditions = [
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9], 
#     [1, 4, 7], 
#     [2, 5, 8], 
#     [3, 6, 9], 
#     [1, 5, 9], 
#     [3, 5, 7]
# ]

# turn = "X"

# def printBoard():
#     index = 0
#     for i in range(3):
#         print("-" * 7)
#         message = ""
#         for j in range(3):
#             index += 1
#             message = message + "|" + str(board[index - 1])
#         message = message + "|"
#         print(message)

# def ask(ans):
#     if ans in board:
#         board[int(ans) + 1] = turn
#         printBoard()
#     else: 
#         print("Error")
#         ask(input("Choose a number "))

# def checkBoard():
#     for condition in conditions:
#         won = 1
#         for i in condition:
#             if board[i - 1] == turn:
#                 won = 0
#         if won == 1:
#             winner = turn


# printBoard()
# for i in range(9):
    
#     ask(input("Choose a number "))
#     if turn == "X":
#         turn = "O"
#     else:
#         turn = "X"
#     printBoard()
#     checkBoard()