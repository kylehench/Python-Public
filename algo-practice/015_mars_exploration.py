#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
# Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, s, determine how many letters of the SOS message have been changed by radiation.

def marsExploration(s):
  return sum([c1 != c2 for c1, c2 in zip(s, 'SOS'*int(len(s)/3))])

if __name__ == '__main__':

  s = 'SOSSOT'
  print(marsExploration(s))


