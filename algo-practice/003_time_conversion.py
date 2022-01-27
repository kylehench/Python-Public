#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Sample Input
# 07:05:45PM
# Sample Output
# 19:05:45

def timeConversion(s):
    hour = int(s[0:2])
    if s[-2:] == 'PM':
        if hour != 12:
            hour += 12
    elif hour == 12:
        hour = 0
    hour = str(hour).zfill(2)
    return hour + s[2:-2]

if __name__ == '__main__':

    s = input()

    print(timeConversion(s))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')12

#     s = input()

#     result = timeConversion(s)

#     fptr.write(result + '\n')

#     fptr.close()