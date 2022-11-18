# You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

# Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

def solution(value1, weight1, value2, weight2, maxW):
  combinations = [(0, 0), (0, 1), (1, 0), (1, 1)]
  values = [0] + [value1*i + value2*j for i, j in combinations if weight1*i + weight2*j <= maxW]
  return max(values)