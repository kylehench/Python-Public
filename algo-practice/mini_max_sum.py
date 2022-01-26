#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):
    min_arr = arr.copy()
    min_arr.remove(max(arr))
    max_arr = arr.copy()
    max_arr.remove(min(arr))
    print(sum(min_arr), sum(max_arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)