# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

def fractionToDecimal(self, numerator: int, denominator: int) -> str:
  ans = []
  if numerator/denominator<0:
    ans.append('-')
  numerator = abs(numerator)
  denominator = abs(denominator)
  ans.append(str(int(numerator/denominator)))
  remainder = abs(numerator%denominator)
  if remainder>0:
    ans.append('.')
  remainderLoc = {}
  remainder *= 10
  while remainder!=0 and len(ans)<1e4:
    if remainder in remainderLoc:
      i = remainderLoc[remainder]
      ans = ans[:i] + ['('] + ans[i:]
      ans.append(')')
      break
    remainderLoc[remainder] = len(ans)
    ans.append(str(int(remainder/denominator)))
    remainder = (remainder%denominator)*10
  return ''.join(ans)