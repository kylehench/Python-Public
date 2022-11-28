# Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

def solution(n):
  digits = [int(ch) for ch in str(n)]
  length = len(digits)
  for i in range(len(digits)-1):
    if digits[i] < digits[i+1]:
      del digits[i]
      break
  if len(digits)==length:
    del digits[-1]
  return int(''.join(str(ch) for ch in digits))