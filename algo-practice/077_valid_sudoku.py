# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]
    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val=='.': continue
        
        # check if value unique in row
        if val in rows[r]: return False
        rows[r].add(val)
        
        # check if value unique in column
        if val in cols[c]: return False
        cols[c].add(val)
        
        # check if value unique in square
        square_idx = c//3 + (r//3)*3
        if val in squares[square_idx]: return False
        squares[square_idx].add(val)
            
    return True