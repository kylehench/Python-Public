# You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.

def cum_sum_rev(arr):
  curr_sum = 0
  cum_sum = []
  for x in arr[::-1]:
    curr_sum += x
    cum_sum.append(curr_sum)
  return cum_sum[::-1]

def equalStacks(h1, h2, h3):
  cum_sum_combined = cum_sum_rev(h1) + cum_sum_rev(h2) + cum_sum_rev(h3)
  cum_sum_combined.sort()
  prev = 0
  count = 0
  for x in cum_sum_combined[::-1]:
    if x == prev:
      count += 1
    else:
      count = 0
    prev = x
    if count == 2:
      return prev
  return 0

test_cases = (
  ([1,2,1,1],[1,1,2],[1,1]),
  ([1,1,1,1,2],[3,7],[1,3,1]),
)
for case in test_cases:
  print(equalStacks(*case))