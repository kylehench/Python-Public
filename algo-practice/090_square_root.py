# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

class Solution:
  def mySqrt(self, x: int) -> int:
    if x == 1:
      return 1
    low = 0
    high = x
    while 1:
      mid = (low + high)//2
      square = mid*mid
      square_next = (mid+1) * (mid+1)
      if square <= x and square_next > x:
        break
      elif square < x:
        low = mid
      else:
        high = mid
    return mid