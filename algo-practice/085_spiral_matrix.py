# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution1:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    width = len(matrix[0])
    height = len(matrix)
    r = 0
    c = -1
    vector = (0, 1)
    res = []
    for _ in range(width*height):
      r_next = r + vector[0]
      c_next = c + vector[1]
      if r_next >= 0 and r_next < height and c_next >= 0 and c_next < width and matrix[r_next][c_next] != None:
        pass
      else:
        vector = (vector[1], -vector[0])
        r_next = r + vector[0]
        c_next = c + vector[1]
      r = r_next
      c = c_next
      res.append(matrix[r][c])
      matrix[r][c] = None
    return res
    
class Solution2:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = []
    while matrix:
      res.extend(matrix.pop(0))
      if matrix and matrix[0]:
        for r in matrix:
          res.append(r.pop())
      if matrix:
        res.extend(matrix.pop()[::-1])
      if matrix and matrix[0]:
        for r in matrix[::-1]:
          res.append(r.pop(0))
        
    return res