# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

class Solution:
  def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    height = len(board)
    width = len(board[0])
    adjacent = [(0,1),(0,-1),(1,0),(-1,0)]
    if len(board)<3:
        return
    inner_oes = set([(i//(width-2)+1, i%(width-2)+1) for i in range((height-2)*(width-2)) if board[i//(width-2)+1][i%(width-2)+1]=='O'])
    protected = set()
    borders = (((0,0),(0,width-1)), ((0,width-1),(height-1,width-1)), ((height-1,width-1),(height-1,0)), ((height-1,0),(0,0)))
    vector = (0,1)
    v_inner = (1,0)
    # ring index 0 = outermost ring
    for start, end in borders:
      # protect corners
      if board[start[0]][start[1]]=="O":
          protected.add((start[0],start[1]))
          # squares.remove((start[0],start[1]))

      # square runs border
      square = (start[0]+vector[0], start[1]+vector[1])
      while 1:
        if square[0]==end[0] and square[1]==end[1]:
          break
        if board[square[0]][square[1]]=='O':
          protected.add((square[0], square[1]))
          square_inner = (square[0]+v_inner[0], square[1]+v_inner[1])
          if square_inner in inner_oes:
            stack = [square_inner]
            inner_oes.remove(square_inner)
            while len(stack)>0:
              r, c = stack.pop()
              protected.add((r,c))
              for i,j in adjacent:
                if (r+i, c+j) in inner_oes:
                  stack.append((r+i, c+j))
                  inner_oes.remove((r+i, c+j))

        square = (square[0]+vector[0], square[1]+vector[1])
        
        # rotate vectors before next iteration
        vector = (vector[1], -vector[0])
        v_inner = (v_inner[1], -v_inner[0])

    for r in range(height):
      for c in range(width):
        if board[r][c]=='O' and (r,c) not in protected:
          board[r][c] = 'X'