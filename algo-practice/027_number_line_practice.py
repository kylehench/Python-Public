# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
# Example
# After one jump, they are both at , (, ), so the answer is YES.
# Function Description
# Complete the function kangaroo in the editor below.
# kangaroo has the following parameter(s):
# int x1, int v1: starting position and jump distance for kangaroo 1
# int x2, int v2: starting position and jump distance for kangaroo 2
# Returns
# string: either YES or NO
# Constraints:
# 0 <= x1 <= x2 <= 10000
# 1 <= v1 <= 10000
# 1 <= v2 <= 10000

def kangaroo(x1, v1, x2, v2):
  if v2 >= v1:
    return "NO"
  dx = x2-x1
  dv = v2-v1
  t_intersect = dx/dv
  if int(t_intersect) == t_intersect:
    return "YES"
  return "NO"

test_case = [1,2,2,1]
print(kangaroo(*test_case)) # should return 'YES'