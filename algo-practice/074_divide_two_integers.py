class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    res_positive = (dividend > 0) == (divisor >0)
    if dividend < 0: dividend = -dividend
    if divisor < 0: divisor = -divisor
    table = [(1, divisor)]
    while table[-1][1] < dividend:
      table.append((table[-1][0]+table[-1][0], table[-1][1]+table[-1][1]))
    table.reverse()
    total = 0
    quotient = 0
    for a, b in table:
      if b <= dividend-total:
        quotient += a
        total += b
    if not res_positive: quotient = -quotient
        
    # insure quotient is in the 32-bit range
    if quotient > 0 and quotient > 2**31-1: quotient = 2**31-1
    if quotient < 0 and quotient < -2**31: quotient = -2**31
    return quotient