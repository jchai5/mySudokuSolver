# mySudokuSolver

This sudoku solver takes in a grid 
represented by list of lists. The empty spaces are 
represented as -1 and the algorithm uses backtracking
to recursively find the correct number 
to place. 

STEPS:
1) First we find the next empty space 
represented by -1.
   
2) Then we check if the number we are placing is
is valid. If it is valid, then we place the number. 
   
3) solve_sudoku returns true if we have solved the puzzle.
If we haven't solved the puzzle, then we need to backtrack and 
   change the current space to -1 so we can recursively
   backtrack. 
   
# autoSudoku
In this sudoku solver, it implements PyAutoGui which
enables the program to control the inputs. 
https://pyautogui.readthedocs.io/en/latest/

The program is similar with mySudokuSolver, except after finding the 
solution, we use PyAutoGui to enter the answer for us on the website.

# HOW TO USE: 
Open autoSudoku.py and run it.
1) Enter the sudoku puzzle, row by row. (Empty inputs represents 0, make sure no spacing e.g. 001020050070)
2) On the last (9th) row, make sure to have 
the website open to prepare for the code.

3) When pressed enter, switch to browser website (5 second timer before program starts)
and click on the beginning of the puzzle (first square).
   
4) The program should autofill the answer.

Example sudoku website: 
https://sudoku.com/expert/

Log:
1) (9/July) The program only works on sudoku.com for some reason. 
After the 9th 