#! /bin/python


# this function checks if a queen can be placed in location (col,row)
def isValid(col, row, chessBoard):
    # check if there is a queen in the same row
    for i in range(col):
        if chessBoard[row][i] == 1:
            return False

    # Check if there is a quen in the same column
    for i in range(row):
        if chessBoard[i][col] == 1:
            return False

    # check if there is a queen in the same diagonal
    for i in range(8):
        for j in range(8):
            if (i + j == col + row) or (i - j == col - row):
                if chessBoard[j][i] == 1:
                    return False
    return True


# initialize chessboard
N = 8
chessBoard = []
for i in range(N):
    chessBoard.append([])
    for j in range(N):
        chessBoard[i].append(0)

# place a queen in the upper left corner of the board
chessBoard[1][1] = 1
chessBoard[0][4] = 1
chessBoard[2][6] = 1

columnIndex = int(input("Enter a column index:\n"))
rowIndex = int(input("Enter a row index:\n"))


print(
    "Placing a queen at column",
    columnIndex,
    "row",
    rowIndex,
    ":",
    isValid(columnIndex, rowIndex, chessBoard),
)
