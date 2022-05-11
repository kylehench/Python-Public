# We define a magic square to be an nxn matrix of distinct positive integers from 1 to n**2 where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

# You will be given a 3x3 matrix  of integers in the inclusive range [1,9]. We can convert any digit  to any other digit  in the range  at cost of abs(a-b). Given , convert it into a magic square at minimal cost. Print this cost on a new line.

# Note: The resulting magic square must contain distinct integers in the inclusive range .


import itertools

def formingMagicSquare(s):
  # for 3x3 magic square, there is only one base solution that can be rotated and flipped for 8 total solutions
  magic = [(8,3,4),(1,5,9),(6,7,2)]
  s_flat = list(itertools.chain(*s))

  min_cost = None
  for i in range(8):
    m = magic
    if i>3:
      m = m[::-1] # flip
    for j in range(i%4):
      m = list(zip(*m[::-1])) # rotate
    m_flat = list(itertools.chain(*m))
    
    # calculate cost
    cost = sum(abs(a-b) for a,b in zip(s_flat, m_flat))
    if min_cost==None or cost<min_cost:
      min_cost = cost

  return min_cost

test = [[5,3,4],[1,5,8],[6,4,2]]

print(formingMagicSquare(test))