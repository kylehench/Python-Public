# Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.
# Given an integer, find its digit degree.

def solution(n):
  s = str(n)
  count = 0
  while len(s) > 1:
    s = str(sum(int(ch) for ch in s))
    count += 1
  return count