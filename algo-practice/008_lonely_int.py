#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
# Given an array of integers, where all elements but one occur twice, find the unique element.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    int_dict = {}
    for i in a:
        if str(i) not in int_dict:
            int_dict[str(i)] = 1
        else:
            int_dict[str(i)] += 1
    return [int(key) for key in int_dict if int_dict[key]==1][0]
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()