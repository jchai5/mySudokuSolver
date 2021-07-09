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
   