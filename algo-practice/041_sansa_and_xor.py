# Sansa has an array. She wants to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the values thus obtained. Determine this value.

# notes: if the number of elements is even, they all cancel out. If it is odd, even indices cancel (starting with 1)

import math
import os
import random
import re
import sys

def sansaXor(arr):
  if len(arr)%2==0: return 0
  res = 0
  for i in range(0, len(arr), 2):
    res = res^arr[i]
  return res

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  t = int(input().strip())

  for t_itr in range(t):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = sansaXor(arr)

    fptr.write(str(result) + '\n')

  fptr.close()
