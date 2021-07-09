import pyautogui as pg
import numpy as np
import time

grid = []
def user_input():
    """
    Get the user-input of the sudoku puzzle, row by row. Enter 0 for empty space.
    :return: None
    """
    while True:
        row = list(input('Row:')) # string
        ints = []
        for n in row:
            ints.append(int(n)) # convert to int
        grid.append(ints)

        if len(grid) == 9:
            break
        print('Row ' + str(len(grid)) + ' Complete')
    time.sleep(2)

def find_next_empty(puzzle):
    """
    Find the next row and col on the puzzle that is not filled yet, 0 (open spaces as 0).
    Return row, col tuple (or (None, None) if there is none).

    Keep in mind that we are using 0-8 for our indices

    :param puzzle: the sudoku grid
    :return: row, col if there is an empty space, else None
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None,None

def is_valid(puzzle, guess, row, col):
    """
    figures out whether the guess at the row/col of the puzzle is a valid guess
    :param puzzle: grid of sudoku puzzle
    :param guess: the number to guess
    :param row: the row index of the current space
    :param col: the column index of the current space
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

def browser_input(puzzle):
    """
    Automates the inputs onto the browser/website of the sudoku puzzle. Make sure to start
    at the beginning of the puzzle even when there is already a number
    :param puzzle: the solved sudoku puzzle
    :return: None
    """
    final = []
    str_fin = []
    for i in range(9):
        final.append(puzzle[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')

def solve_sudoku():
    """
    We will solve the sudoku puzzle using backtracking.
    The puzzle is a list of lists, where each inner list is a row in our sudoku.
    We will return if a solution exists.
    :return: None
    """
    global grid # the sudoku puzzle

    puzzle = grid
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
            if solve_sudoku(): # if true
                return True

        # step 5: if not valid OR if our guess does not solve the
        # puzzle, then we need to backtrack and try a new puzzle
        puzzle[row][col] = 0 # reset the guess

    # step 6: if none of the numbers that we try work, then this
    # puzzle is UNSOLVABLE:
    return False


if __name__ == "__main__":
    user_input() # manual input sudoku puzzle
    print(solve_sudoku()) # returns true if there is solution
    browser_input(grid) # inputs the answer into the browser

    # print out the board
    length = len(grid)
    for i in range(length):
        print(grid[i])