

def Horizontal_Win(board):
    for row in board: #Horizontal winner
        if row.count(row[0])==len(row) and row[0] != 0:
            print(f"player {row[0]} ")
            return True

def Vertical_win(board):
    
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0]!= 0:
            print(f"player {check[0]} ")
            return True

def Diagonal_win(board, n=3):
    check = []
    check2 = []
    for i in range(n):
        check.append(board[i][i])
        check2.append(board[n-i-1][i])
    if check.count(check[0]) == len(check) and check[0]!=0:
        print(f"player {check[0]} win")
        return True
    if check2.count(check2[0]) ==len(check2) and check2[0]!=0:
        #print(f"player {check2[0]} win")
        return True
        
    


def Win(board,n=3):
    if (Horizontal_Win(board)):
        return True
    if (Vertical_win(board)):
        return True
    if Diagonal_win(board,n):
        return True



def Print_board(board, n=3):
    
    s = ''
    for i in range(n):
        s += f"{i}   "
    print(f"    {s}")
    for count, row in enumerate(board):
        realXO=' '
        for i in row:
            if i ==0:
                realXO += "|   "
            elif i == 1:
                realXO += "| X "
            elif i == 2:
                realXO += "| O "
        print(f"{count}{realXO}")


def Change_board(board, row = 0, column = 0,player =0, n=3):
    board[row][column] = player
    Print_board(board,n)
    return board

#------------------START------------------#
NewGame = True
while NewGame:
    
    n = int(input("what size you want 3,4 or 5..."))
    GameBoard = [[0 for x in range(n)] for i in range(n)]
    Print_board(GameBoard,n)
    player = 0
    while not Win(GameBoard,n):
        
        try:
            checkInput = True
            while(checkInput):
                row = int(input("nhap hang "))
                
                col = int(input("nhap cot "))
                
                if GameBoard[row][col] != 0:
                    
                    print("cheating... input again")
                    continue
                break
            GameBoard = Change_board(GameBoard,row,col,player%2 +1,n)
            Print_board(GameBoard,n)
            player +=1
        except:
            print("someting wrong, input again")
            player -= 1
            continue
    Restart = input("do you want restart (y\\n)")
    if Restart == 'y':
        print("reset")
    elif Restart == n:
        print("Byeeee")
        break
    else:
        print("Let's make a new one")    
    
            
    
    
