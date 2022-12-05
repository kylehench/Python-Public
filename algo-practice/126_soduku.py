# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

# This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

def solution(grid):
  correct_set = set(i for i in range(1, 10))
  def check_square(r, c):
    return set(grid[r+i//3][c+i%3] for i in range(9)) == correct_set
  if any((
    any((
      set(row) != correct_set for row in grid
    )),
    any((
      set(grid[r][c] for r in range(9)) != correct_set for c in range(9)
    )),
    any((
      check_square((i//3)*3, (i%3)*3)==False for i in range(9)
    ))
  )):
    return False
  return True