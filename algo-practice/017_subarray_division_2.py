# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

def birthday(s, d, m):
  segment_count = 0
  n = len(s)
  total = sum(s[0:m])
  if total==d:
    segment_count+=1
  for i in range(n-m):
    total += s[i+m]-s[i]
    if total==d:
      segment_count+=1
  return segment_count

if __name__ == '__main__':

  test_cases = [[[2,2,1,3,2],[4,2]],
    [[1,2,1,3,2],[3,2]],
    [[2,3,4,4,2,1,2,5,3,4,4,3,4,1,3,5,4,5,3,1,1,5,4,3,5,3,5,3,4,4,2,4,5,2,3,2,5,3,4,2,4,3,3,4,3,5,2,5,1,3,1,4,2,2,4,3,3,3,3,4,1,1,4,3,1,5,2,5,1,3,5,4,3,3,1,5,3,3,3,4,5,2],[26,8]],
    [[4,1,4,3,3,5,1,2,4,2,5,1,5,1,4,1,3,1,5,2,2,2,1,1,3,2,5,3,1,5,4,5,2,2,1,1,2,2,4,5,4,1,5,2,1,1,2,2,1,3,2,4,4,1,3,2,2,3,1,5,4,4,1,4,2,1,2,1,5,1,3,3,4,2,1,5,5,4,2,2,3,3,4,3,1,2,1,2,4,3],[16,7]]]
  for case in test_cases:
    s = case[0]
    first_multiple_input = case[1]
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    print(s, d, m)
    print(birthday(s, d, m))
