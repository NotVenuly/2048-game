import random
boardHeight = 4
boardLength = 4

def StartGame():
    board = []
    for row in range(boardHeight):
        board.append([0]*boardLength)
    print("Commands: ")
    print("'W': Move Up")
    print("'S': Move Down")
    print("'A': Move Left")
    print("'D': Move Right")
    AddRandom2(board)
    return board

def AddRandom2(board):

    tries = 0
    while tries < 20:
        row = random.randint(0,len(board)-1)
        column = random.randint(0,len(board[0])-1)
        if (board[row][column] == 0):
            board[row][column] = 2
            for row in board:
                print(row)
            return
        tries +=1
    row, column = FindEmpty(board)
    if row is not None and column is not None:
        board[row][column] = 2
    
    for row in board:
        print(row)


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


def compress(board):

    changed = False
    new_board = []
    for row in range(boardHeight):
        new_board.append([0] * boardLength)
        
    for row in range(boardHeight):
        pos = 0
        for column in range(boardLength):
            if(board[row][column] != 0):
                new_board[row][pos] = board[row][column]
                
                if(column != pos):
                    changed = True
                pos += 1

    return new_board, changed

def merge(board):
    
    changed = False
    
    for row in range(boardHeight):
        for column in range(boardLength-1):

            if(board[row][column] == board[row][column + 1] and board[row][column] != 0):

                board[row][column] = board[row][column] * 2
                board[row][column + 1] = 0
                changed = True

    return board, changed

def reverse(board):
    new_board =[]
    for row in range(boardHeight):
        new_board.append([])
        for column in range(boardLength):
            new_board[row].append(board[row][3 - column])
    return new_board

def transpose(board):
    new_board = []
    for row in range(boardHeight):
        new_board.append([])
        for column in range(boardLength):
            new_board[row].append(board[column][row])
    return new_board

def move_left(grid):

    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    
    changed = changed1 or changed2

    new_grid, temp = compress(new_grid)
    return new_grid, changed

def move_right(grid):

    new_grid = reverse(grid)
    new_grid, changed = move_left(new_grid)

    new_grid = reverse(new_grid)
    return new_grid, changed

def move_up(grid):

    new_grid = transpose(grid)
    new_grid, changed = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

def move_down(grid):
    new_grid = transpose(grid)
    new_grid, changed = move_right(new_grid)

    new_grid = transpose(new_grid)
    return new_grid, changed
