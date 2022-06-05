import random, sys

BLANK = "  "


def main():
    print("""Sliding Tile Puzzle, by Al Sweigart 

    Once you press enter, the puzzle will solve automatically""")
    input("Press Enter to begin...")

    gameBoard = getNewPuzzle()

    while True:
        x = 0
        for i in range(40):
            displayBoard(gameBoard)
            playerMove = makeRandomMove(gameBoard)
            makeMove(gameBoard, playerMove)
            x += 1
            print(x)

        if gameBoard == getNewBoard():
            print("You won!")
            sys.exit()
        else:
            tile = input("Do you wish to continue? ")
            if tile.lower() == "yes":
                for i in range(40):
                    displayBoard(gameBoard)
                    playerMove = makeRandomMove(gameBoard)
                    makeMove(gameBoard, playerMove)
                    x += 1
                    print(x)
                if gameBoard == getNewBoard():
                    print("You won!")
                    sys.exit()
            elif tile.lower() == "no":
                print("You failed! Good Luck for next time ;)")
                sys.exit()


def getNewBoard():
    """Return a list of lists that represents a new tile puzzle"""
    return [['1 ', '6 ', '11', '16', '21'], ['2 ', '7 ', '12', '17', '22'],
            ['3 ', '8 ', '13', '18', '23'], ['4 ', '9 ', '14', '19', '24'], ['5 ', '10', '15', '20', BLANK]]


def displayBoard(board):
    """Display the given board on the screen."""

    labels = [board[0][0], board[1][0], board[2][0], board[3][0], board[4][0],
              board[0][1], board[1][1], board[2][1], board[3][1], board[4][1],
              board[0][2], board[1][2], board[2][2], board[3][2], board[4][2],
              board[0][3], board[1][3], board[2][3], board[3][3], board[4][3],
              board[0][4], board[1][4], board[2][4], board[3][4], board[4][4]]
    boardtoDraw = """
  +------+------+------+------+------+
 |      |      |      |      |      |
 |  {}  |  {}  |  {}  |  {}  |  {}  |
 |      |      |      |      |      |
 +------+------+------+------+------+
 |      |      |      |      |      |
 |  {}  |  {}  |  {}  |  {}  |  {}  |
 |      |      |      |      |      |
 +------+------+------+------+------+
 |      |      |      |      |      |
 |  {}  |  {}  |  {}  |  {}  |  {}  |
 |      |      |      |      |      |
 +------+------+------+------+------+
 |      |      |      |      |      |
 |  {}  |  {}  |  {}  |  {}  |  {}  |
 |      |      |      |      |      |
 +------+------+------+------+------+   
 |      |      |      |      |      |
 |  {}  |  {}  |  {}  |  {}  |  {}  |
 |      |      |      |      |      |
 +------+------+------+------+------+   

""".format(*labels)
    print(boardtoDraw)


def findBlankSpace(board):
    """Return an (x, y) tuple of the blank space's location"""
    for x in range(5):
        for y in range(5):
            if board[x][y] == "  ":
                return (x, y)


def askForPlayerMove(board):
    """Let the player select a tile to slide"""
    blankx, blanky = findBlankSpace(board)

    w = "W" if blanky != 4 else " "
    a = "A" if blankx != 4 else " "
    s = "S" if blanky != 0 else " "
    d = "D" if blankx != 0 else " "

    while True:
        print("Enter let it play (or QUIT")

        response = input("> ").upper()
        if response == "QUIT":
            sys.exit()
        else:
            return response


def makeMove(board, move):
    """Carry out the given move on the given board."""
    # Note: This function assumes that the move is valid.
    bx, by = findBlankSpace(board)

    if move == 'W':
        board[bx][by], board[bx][by + 1] = board[bx][by + 1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx + 1][by] = board[bx + 1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by - 1] = board[bx][by - 1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx - 1][by] = board[bx - 1][by], board[bx][by]


def makeRandomMove(board):
    """Perform a slide in a random direction."""
    blankx, blanky = findBlankSpace(board)

    validMoves = []
    if blanky != 4:
        validMoves.append("W")
    if blankx != 4:
        validMoves.append("A")
    if blanky != 0:
        validMoves.append("S")
    if blankx != 0:
        validMoves.append("D")

    makeMove(board, random.choice(validMoves))


def getNewPuzzle(moves=200):
    """Get a new puzzle by making random slides from a solved state."""
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)
    return board


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
