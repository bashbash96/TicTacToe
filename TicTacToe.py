DIM = 3
NUM_OF_PLAYERS = 2

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

        player = (player + 1) % NUM_OF_PLAYERS
        counter -= 1

    if counter < 0:  # if the counter reached to zero so the game ended with draw
        print('The game has end with draw!')


def getMove(player):
    """
    get valid row and column indexes for next move
    :param player: the current player number
    :return: row, column indexes
    """
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
    """
    check if index is valid
    :param num: index
    :return:
    """
    if num < 0 or num >= DIM:
        return False
    return True


def printBoard(board):
    """
    print current game board
    :param board:
    :return:
    """
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
    """
    check if after current move any one has won
    :param board: game board
    :param row: row index of current move
    :param col: column index of current move
    :return: True / False
    """
    if checkVertical(board, row, col) or checkHorizontal(board, row, col) or checkDiagonal(board):
        return True
    return False


def checkHorizontal(board, row, col):
    """
    check if the current player won horizontally
    :param board: game board
    :param row: row index of current move
    :param col: column index of current move
    :return: True / False
    """
    currVal = board[row][col]
    if currVal != 'X' and currVal != 'O':
        return False
    for col2 in range(DIM):
        if currVal != board[row][col2]:
            return False
    return True


def checkVertical(board, row, col):
    """
    check if current player won vertically
    :param board: game board
    :param row: row index of current move
    :param col: column index of current move
    :return: True / False
    """
    currVal = board[row][col]
    if currVal != 'X' and currVal != 'O':
        return False
    for row2 in range(DIM):
        if currVal != board[row2][col]:
            return False
    return True


def checkDiagonal(board):
    """
    check if current player won in each of the two main diagonals
    :param board: game board
    :return: True / False
    """
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
    """
    put move char (X or O) in row and column indexes if and only if there is
    no chars in the specified row and column
    :param board: game board
    :param row: row index of current move
    :param col: column index of current move
    :param move: curr move value (X or O)
    :return: True / False
    """
    if board[row][col] != 'X' and board[row][col] != 'O':
        board[row][col] = move
        return True
    else:
        return False


main()
