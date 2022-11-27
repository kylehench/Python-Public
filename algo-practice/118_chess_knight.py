# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

# The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

def solution(cell):
  # seed first two vectors
  vectors = [(1,2), (2,1)]
  # rotate and append seed 3 times
  for _ in range(3):
    for _ in range(2):
      vectors.append((vectors[-2][1], -vectors[-2][0]))
  x = ord(cell[0]) - ord('a')
  y = int(cell[1]) - 1
  return sum(0<=x+x1<=7 and 0<=y+y1<=7 for x1, y1 in vectors)