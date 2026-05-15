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
        if board[row][column] == 0:
            board[row][column] = 2
            return
        tries +=1


def PrintBoard(board):
    for line in board:
        print(line)

if __name__ == "__main__":
    StartGame()