import random
boardHeight = 4
boardLength = 4

def StartGame():
    board = []
    for i in range(boardHeight):
        board.append([0]*boardLength)
    print("Commands: ")
    print("'W': Move Up")
    print("'S': Move Down")
    print("'A': Move Left")
    print("'D': Move Right")
    PrintBoard(board)

def AddRandom2(board):

    tries = 0
    while tries < 20:
        row = random.randint(0,len(board)-1)
        column = random.randint(0,len(board[0])-1)
        if (board[row][column] == 0):
            board[row][column] = 2
            return
        tries +=1
    row, column = FindEmpty(board)
    if row is not None and column is not None:
        board[row][column] = 2


def FindEmpty(board):
    for row in range(boardHeight):
        for column in range(boardLength):
            if (board[row][column] == 0):
                return row, column  
    return None, None 

def CheckForWin(board):
    for row in range(boardHeight):
        for column in range(boardLength):
            if (board[row][column] == 2048):
                return 'YOU WIN'
            elif(board[row][column]== 0):
                return 'GAME NOT OVER'

                
                
    for row in range(boardHeight-1):
        for column in range(boardLength-1):
            if(board[row][column] == board[row + 1][column] or 
               board[row][column] == board[row][column + 1]):
                return 'GAME NOT OVER'

    for column in range(boardLength-1):
        if(board[3][column]== board[3][column + 1]):
            return 'GAME NOT OVER'

    for row in range(boardHeight-1):
        if(board[row][boardLength-1]== board[row + 1][boardLength-1]):
            return 'GAME NOT OVER'
        
    return 'LOST'

def PrintBoard(board):
    for line in board:
        print(line)

if __name__ == "__main__":
    StartGame()