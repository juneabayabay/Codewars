
def chessboard(rows, columns):
    board = [] # create an empty list to store the board

    for i in range(rows): # outer loap control the number of rows
        row = [] # create an empty list to store the row

        for j in range(columns): # inner loop control the number of columns
            if (i + j) % 2 == 0: # check if the sum of the row and column is even
                row.append('O') # add 'O' to the row if the sum is even
            else:
                row.append('X') # add 'X' to the row if the sum is odd

        board.append(row) # add the row to the board

    return board # return the board


print(chessboard(3, 4)) # print the board
