#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
# Given an integer, flip all the bits and return the result as an unsigned integer
#

def flippingBits(n):
  binary = f'{n:032b}' # 0 padded 32 digit binary format
  return int(''.join(['0' if char=='1' else '1' for char in binary]), 2)

input = [3, 2147483647, 1, 0]
for x in input:
  print(flippingBits(x))