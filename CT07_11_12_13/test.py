def initboard():
    board = []

    for i in range(3):
        row = []

        for a in range(3):
            row.append(" ")

        board.append(row)

    return board

def printboard(argboard):
    count = 1
    for row in argboard:

        for col in row:

            if col == " ":
                print(f"| {count} ", end="")
            else:
                print(f"| {col} ", end="")

            if count % 3 == 0:
                print("|")
                print("-" * 13)
            count += 1


def get_player_move(argboard, playerNOW):
    while True:
        move = input(f"Player {playerNOW}, Ples enter a number from 1, 9: ")

        if move.isdigit():
            move = int(move)
            # pass
            if move >= 1 and move <= 9:
                move = move - 1
                row = move // 3
                col = move % 3
                print(f"row = {row}, col = {col}")


                if argboard[row][col] == " ":
                    argboard[row][col] = (playerNOW)
                    break
                else:
                    print(f"{move+1} is already taken. Choose another please")



                # pass
            else:
                print("Eh! Siao Dabor u butter pult an legit numble lerh. Isf u don then i suport adove hiter.")
        else:
            print("Eh! Siao Zabor ples pult a legit numble lerh. Isf u don then i cal polis and sgsecure.")
    return argboard


def getcurrentplayer(player):
    print(f"getting current player: {player}")
    if player == "X":
        return "O"
    else:
        return "X"


def checkwin(argboard):
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

def checktie(argboard):
    for row in argboard:
        for cell in row:
            if cell == " ":
                return False
    
    return True

# 1. Check if AI can win in the next move == take that move.
# 2. Check if player can win in next move == block it.
# 3. If center is empty == take center.
# 4. If a corner is empty == take a corner.
# 5. Else == take any available space.




def get_aimove(board, currplayer):
    # 1. Check if AI can win in the next move == take that move.
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] == currplayer # This will be AI value.

                if checkwin(board):
                    print("inside ai move 111")
                    return board
                else:
                    print(f" 111 Move i:{i} j:{j}")
                    board[i][j] == " "
    print("test")
    # 2. Check if player can win in next move == block it.
    opponent = "X" # which means you
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = opponent # simulate player maving a move

                
                if checkwin(board):
                    print(f" 222 Move i:{i} j:{j}")
                    print(f"inside ai move 222 {currplayer}")
                    board[i][j] = currplayer # Ai will make a move here
                    return board
                else:
                    print(f" 222 Move i:{i} j:{j}")
                    board[i][j] == " " #Ai will reset for the next value

    # 3. If center is empty == take center.
    if board[1][1] == " ":
        print("inside ai move 333")
        board[1][1] = currplayer # computer will move to center
        return board
    
    # 4. If a corner is empty == take a corner.



    
board = initboard()
currentplayer = " "

while True:
    printboard(board)

    currentplayer = getcurrentplayer(currentplayer)

    if currentplayer == "X":
        board = get_player_move(board, currentplayer)
        print("lalala")
    else:
        print("bababa")
        board = get_aimove(board, currentplayer)

    print(board)
    if checkwin(board):
        print("*"*20)
        print(f"Player {currentplayer} wins!")
        printboard(board)
        break
    elif checktie(board):
        print("*"*20)
        print("it is a tie. Say bye bye to lim beh")
        printboard(board)
        break



    
