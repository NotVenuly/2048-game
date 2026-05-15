import Logic

if __name__ == '__main__':
        board = Logic.StartGame()

while(True):

    x = input("Press the command : ")
    if(x == 'W' or x == 'w'):

        board, flag = Logic.move_up(board)
        status = Logic.CheckForWin(board)
        print(status)

        if(status == 'GAME NOT OVER'):
            Logic.AddRandom2(board)
        else:
            break

    elif(x == 'S' or x == 's'):
        board, flag = Logic.move_down(board)
        status = Logic.CheckForWin(board)
        print(status)
        if(status == 'GAME NOT OVER'):
            Logic.AddRandom2(board)
        else:
            break

    elif(x == 'A' or x == 'a'):
        board, flag = Logic.move_left(board)
        status = Logic.CheckForWin(board)
        print(status)
        if(status == 'GAME NOT OVER'):
            Logic.AddRandom2(board)
        else:
            break

    elif(x == 'D' or x == 'd'):
        board, flag = Logic.move_right(board)
        status = Logic.CheckForWin(board)
        print(status)
        if(status == 'GAME NOT OVER'):
            Logic.AddRandom2(board)
        else:
            break
    else:
        print("Invalid Key Pressed")