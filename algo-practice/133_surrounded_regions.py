# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

class Solution:
  def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    height = len(board)
    width = len(board[0])

    oes = set()
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == 'O':
          oes.add((i,j))
    adjacent = [(0,1),(0,-1),(1,0),(-1,0)]
    while len(oes)>0:
      safe = False
      region = []
      stack = []
      stack.append(oes.pop())
      while len(stack)>0:
        i, j = stack.pop()
        region.append((i,j))
        if i==0 or i==height-1 or j==0 or j==width-1:
          safe = True
        for x, y in adjacent:
          adj_x = i+x
          adj_y = j+y
          if (adj_x, adj_y) in oes:
            oes.remove((adj_x, adj_y))
            stack.append((adj_x, adj_y))
      if not safe:
        for i, j in region:
          board[i][j] = 'X'