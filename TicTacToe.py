DIM = 3


def main():
    while True:
        ans = input('Wanna play? "y" - Yes | "n" - No \n')
        if ans == 'n':
            break
        elif ans == 'y':
            start()
        else:
            print('please choose form options!')
    print('Bye Bye...')


def start():
    gameBoard = [['0' for j in range(DIM)] for i in range(DIM)]

    counter = DIM * DIM
    player = 0
    while counter >= 0:
        printBoard(gameBoard)
        while True:
            row, col = getMove(player)
            if player % 2 == 0:
                res = makeMove(gameBoard, row, col, 'X')
            else:
                res = makeMove(gameBoard, row, col, 'O')
            if res:
                break
            else:
                print('Error, you cant put value in square with another value...')

        win = checkWin(gameBoard, row, col)

        if win:
            if player % 2 == 0:
                print("Player one has won! Congratulations!")
            else:
                print('Player two has won! Congratulations!')

            break

        player += 1
        counter -= 1

    if counter < 0:
        print('The game has end with draw!')


def getMove(player):
    if player % 2 == 0:
        print('\nPlayer one playing now, where to put "X" ?')
    else:
        print('\nPlayer two playing now, where to put "O" ?')

    while True:
        try:
            row = int(input('Enter row index\n'))
        except:
            print('Invalid row index!')
            continue
        if isValid(row):
            break
        print('Invalid row index!')

    while True:
        try:
            col = int(input('Enter column index\n'))
        except:
            print('Invalid row index!')
            continue
        if isValid(col):
            break
        print('Invalid column index!')

    return row, col


def isValid(num):
    if num < 0 or num >= DIM:
        return False
    return True


def printBoard(board):
    print(end='  ')
    for row in range(DIM):
        print(row, end=' ')
    print()
    for row in range(DIM):
        print(row, end=' ')
        for col in range(DIM):
            print(board[row][col], end=' ')
        print()


def checkWin(board, row, col):
    if checkVertical(board, row, col) or checkHorizontal(board, row, col) or checkDiagonal(board):
        return True
    return False


def checkHorizontal(board, row, col):
    currVal = board[row][col]
    if currVal != 'X' and currVal != 'O':
        return False
    for col2 in range(DIM):
        if currVal != board[row][col2]:
            return False
    return True


def checkVertical(board, row, col):
    currVal = board[row][col]
    if currVal != 'X' and currVal != 'O':
        return False
    for row2 in range(DIM):
        if currVal != board[row2][col]:
            return False
    return True


def checkDiagonal(board):
    currVal = board[0][0]
    if currVal != 'X' and currVal != 'O':
        return False
    res = True
    for row in range(DIM):
        for col in range(row, row + 1):
            if currVal != board[row][col]:
                res = False
    if res:
        return True

    res = True

    currVal = board[0][DIM - 1]
    if currVal != 'X' and currVal != 'O':
        return False
    for row in range(DIM - 1, -1, -1):
        for col in range(DIM - row - 1, DIM - row):
            if currVal != board[row][col]:
                res = False

    return res


def makeMove(board, row, col, move):
    if board[row][col] != 'X' and board[row][col] != 'O':
        board[row][col] = move
        return True
    else:
        return False


main()
