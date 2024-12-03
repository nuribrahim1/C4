board = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]


def renderboard(brd):
    for row in brd:
        for column in row:
            print(f"|{column} ", end = "")
        print("|")

def place(brd):
    column = int(input("select a column"))
    for row in brd[::-1]:
        if row[column] == " ":
            row[column] = 2
            return

def check(brd):
    for row in range(6):
        for column in range(7):
            if brd[row][column] != " ":
                if brd[row][column] == brd[row][column+1] and brd[row][column] == brd[row][column+2] and brd[row][column] == brd[row][column+3]:
                    return True
                else:
                    return False

def playgame(brd):
    print(check(brd))
    while check(brd) != True:
        renderboard(brd)
        place(brd)
        print(check(brd))

playgame(board)

