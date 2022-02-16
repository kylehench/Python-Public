# There are two -element arrays of integers,  and . Permute them into some  and  such that the relation  holds for all  where .
# There will be  queries consisting of , , and . For each query, return YES if some permutation ,  satisfying the relation exists. Otherwise, return NO.
# Example
# A valid  is  and :  and . Return YES.
# Function Description
# twoArrays has the following parameter(s):
# int k: an integer
# int A[n]: an array of integers
# int B[n]: an array of integers
# Returns
# - string: either YES or NO
#!/bin/python3
#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
  A.sort()
  B.sort()
  B.reverse()
  results = [a+b>=k for a,b in zip(A,B)]
  if False in results:
    return 'NO'
  return 'YES'

if __name__ == '__main__':
  tests = [
    { 'k' : int(10),
      'A' : list(map(int, '2 1 3 '.rstrip().split())),
      'B' : list(map(int, '7 8 9 '.rstrip().split())) },
    { 'k' : int(5),
      'A' : list(map(int, '1 2 2 1 '.rstrip().split())),
      'B' : list(map(int, '3 3 3 4 '.rstrip().split())) }
    ]
  for test in tests:
    print(twoArrays(test['k'], test['A'], test['B']))