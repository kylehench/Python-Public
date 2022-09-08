# Implement pow(x, n), which calculates x raised to the power n

class Solution:
  def myPow(self, x: float, n: int) -> float:
    if n==0:
      return 1
    if n > 0:
      base = x
    else:
      base = 1/x
    n = abs(n)
    power = 1
    table = [(1, base)]
    while power <= n/2:
      power = power*2
      table.append((power, table[-1][1]*table[-1][1]))
    table.reverse()
    res = 1
    res_power = 0
    for power, value in table:
      if n-res_power>=power:
        res = res*value
        res_power += power
    return res