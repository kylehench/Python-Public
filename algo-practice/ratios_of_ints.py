#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

def plusMinus(arr):
    total = len(arr)
    pos_cnt = sum([x>0 for x in arr])
    neg_cnt = sum([x<0 for x in arr])
    zero_cnt = sum([x==0 for x in arr])
    print("%.6f" % float(pos_cnt/total))
    print("%.6f" % float(neg_cnt/total))
    print("%.6f" % float(zero_cnt/total))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
