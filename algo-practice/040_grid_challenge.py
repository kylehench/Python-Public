import timeit
# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge1(grid):
  grid = [sorted(list(row)) for row in grid]
  for c_idx in range(len(grid[0])):
    col = [row[c_idx] for row in grid]
    if any([b<a for b,a in zip(col[1:], col[:-1])]):
      return 'NO'
  return 'YES'

def gridChallenge2(grid):
  grid = [sorted(list(row)) for row in grid]
  for r_idx in range(len(grid)-1):
    if any([b<a for b,a in zip(grid[r_idx+1], grid[r_idx])]):
      return 'NO'
  return 'YES'

def gridChallenge3(grid):
  return 'NO' if any(any([b<a for b,a in zip(sorted(list(grid[r_idx+1])), sorted(list(grid[r_idx])))]) for r_idx in range(len(grid)-1)) else 'YES'

test = ['fghij','olmkn','trpqs','xywuv']

print(gridChallenge1(test))
print(gridChallenge2(test))
print(gridChallenge3(test))

print(timeit.timeit(lambda: gridChallenge1(test), number=1000))
print(timeit.timeit(lambda: gridChallenge2(test), number=1000))
print(timeit.timeit(lambda: gridChallenge3(test), number=1000))