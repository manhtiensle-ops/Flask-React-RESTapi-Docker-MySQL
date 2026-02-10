#just learning tic tac toe




def Horizontal_Win(board):
    for row in board: #Horizontal winner
        if row.count(row[0])==len(row) and row[0] != 0:
            return True

def Vertical_win(board):
    
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0]!= 0:
            return True

def Diagonal_win(board, n=3):
    check = []
    for i in range(n):
        check.append(board[i][i])
    if check.count(check[0])== len(check) and check[0]!=0:
        return True
    check2 = []
    for i in range(n):
        check2.append(board[n-i][i])
    if check2.count(check2[0]==len(check2)) and check2[0]!=0:
        return True


def Win(board,n=3):
    if (Horizontal_Win(board)):
        return True
    if (Vertical_win(board)):
        return True
    if Diagonal_win(board,n=3):
        return True



def Print_board(board):
    print("   0  1  2")
    for count, row in enumerate(board):
        print(count, row)


def Change_board(board, row = 0, column = 0):
    board[row][column] = 1
    Print_board(board)
    return board



game_board = [[0,0,1],
              [0,1,0],
              [1,0,0]]
try:
    
    
    if Win(game_board):
        print("win")
except IndexError as e:
    print("shit ",e)
except Exception as e:
    print("holly shit",e)

