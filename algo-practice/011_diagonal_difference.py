#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
  n = len(arr[0])
  diag_1_sum = 0
  diag_2_sum = 0
  for i in range(n):
    diag_1_sum += arr[i][i]
    diag_2_sum += arr[n-1-i][i]
  return abs(diag_1_sum - diag_2_sum)

arr = [[11, 2, 4],
[4, 5, 6],
[10, 8, -12]]

print(diagonalDifference(arr))