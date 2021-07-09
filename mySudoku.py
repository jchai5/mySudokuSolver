def find_next_empty(puzzle):
    """
    Find the next row and col on the puzzle that is not filled yet, -1 (open spaces as -1).
    Return row, col tuple (or (None, None) if there is none).

    Keep in mind that we are using 0-8 for our indices

    :param puzzle:
    :return:
    """

    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    return None,None

def is_valid(puzzle, guess, row, col):
    """
    figures out whether the guess at the row/col of the puzzle is a valid guess
    :param puzzle:
    :param guess:
    :param row:
    :param col:
    :return: True if it is valid, False otherwise
    """
    # let's start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # now we do the column
    col_vals = []
    for i in range(9): # go thru all the row
        col_vals.append(puzzle[i][col]) # get all the vals in that column
    # col_vals = [puzzle[i][col]] for i in range(9) # similar
    if guess in col_vals:
        return False

    # and then check 3x3 grid
    # this is tricky, we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    # EXAMPLE:
    # [ 1 , 2 , 3 ]
    # [ 4 , 5 , 6 ]
    # [ 7 , 8 , 9 ]
    # row_start gets the index of the row
    # if the value is 5, then 5 // 3 = 1, 9 // 3 = 3, 2//3 = 0 ...
    # row_start and col_start tells you which box we are looking at
    # e.g. (5,5) means we are looking at box with starting index
    # row_start = 3, col_start = 3, aka (3,3)
    row_start = (row // 3) * 3 # multiply by 3 to get the actual index
    col_start = (col // 3) * 3
    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if puzzle[row][col] == guess:
                return False

    # if we get here, then we checked all the pass
    return True

def solve_sudoku(puzzle):
    """
    We will solve the sudoku puzzle using backtracking.
    The puzzle is a list of lists, where each inner list is a row in our sudoku.
    We will return if a solution exists.
    :param puzzle:
    :return:
    """
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if theres nowhere left, then we're done because we
    # only allowed valid inputs
    if row is None: # only have to check row because col would be the same
        return True

    # step 2: if there is a place to put a number, then make a guess
    # between 1 and 9
    for guess in range(1,10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle): # if true
                return True

        # step 5: if not valid OR if our guess does not solve the
        # puzzle, then we need to backtrack and try a new puzzle
        puzzle[row][col] = -1 # reset the guess

    # step 6: if none of the numbers that we try work, then this
    # puzzle is UNSOLVABLE:
    return False

def main():
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    print(solve_sudoku(example_board))

    # print out the board
    length = len(example_board)
    for i in range(length):
        print(example_board[i])

if __name__ == "__main__":
    main()