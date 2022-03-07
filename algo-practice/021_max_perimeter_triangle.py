#!/bin/python3

from audioop import reverse
import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
# Given an array of stick lengths, use  of them to construct a non-degenerate triangle with the maximum possible perimeter. Return an array of the lengths of its sides as  integers in non-decreasing order.
# If there are several valid triangles having the maximum perimeter:
# Choose the one with the longest maximum side.
# If more than one has that maximum, choose from them the one with the longest minimum side.
# If more than one has that maximum as well, print any one them.
# If no non-degenerate triangle exists, return .
# Example
# The triplet  will not form a triangle. Neither will  or , so the problem is reduced to  and . The longer perimeter is .
# Function Description
# Complete the maximumPerimeterTriangle function in the editor below.
# maximumPerimeterTriangle has the following parameter(s):
# int sticks[n]: the lengths of sticks available
# Returns
# int[3] or int[1]: the side lengths of the chosen triangle in non-decreasing order or -1
# Input Format
# The first line contains single integer , the size of array .
# The second line contains  space-separated integers , each a stick length.

def maximumPerimeterTriangle(sticks):
  sticks.sort(reverse=True)
  for i in range(len(sticks)-2):
    if sum(sticks[i+1:i+3]) > sticks[i]:
      out = sticks[i:i+3]
      out.sort()
      return out
  return [-1]


if __name__ == '__main__':

    sticks = [1, 2, 3, 4, 5, 10]

    print(maximumPerimeterTriangle(sticks))