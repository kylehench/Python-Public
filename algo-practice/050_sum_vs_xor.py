# Given an integer n, find each x such that:
# 0 <= x <= n
# n + x = n^x
# Return the number of x's satisfying the criteria.

def sumXor(n):
  return 2**(bin(n).count('0')-1) if n != 0 else 1

test_cases = (0,1,4,5,10) # 1,1,4,2,4
for test in test_cases:
  print(sumXor(test))