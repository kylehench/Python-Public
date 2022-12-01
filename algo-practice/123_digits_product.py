# Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

# Example
# For product = 12, the output should be
# solution(product) = 26;
# For product = 19, the output should be
# solution(product) = -1.

def solution(product):
  if product==0:
    return 10
  if product==1:
    return 1
  remain = product
  factors = []
  for num in range(9,1,-1):
    while remain%num==0:
      factors.append(num)
      remain /= num
  if remain != 1:
    return -1
  return int(''.join(str(factor) for factor in sorted(factors)))