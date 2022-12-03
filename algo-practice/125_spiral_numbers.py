# Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

def solution(n):
  res = [[0 for _ in range(n)] for _ in range(n)]
  r, c = 0, 0
  v = [0, 1]
  for i in range(1, n**2+1):
    res[r][c] = i
    if not (0<=r+v[0]<n and 0<=c+v[1]<n and res[r+v[0]][c+v[1]]==0):
      v = [v[1], -v[0]]
    r, c = r+v[0], c+v[1]
  return res