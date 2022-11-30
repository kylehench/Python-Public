# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

def solution(matrix):
  unique = set()
  for r in range(len(matrix)-1):
    for c in range(len(matrix[0])-1):
      unique.add(''.join((str(matrix[r+int(i/2)][c+i%2]) for i in range(4))))
  return len(unique)