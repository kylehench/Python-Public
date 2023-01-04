# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

def partition1(s):
  def is_palindrome(s):
    return s==s[::-1]

  def partition_helper(substrings, i):
    res = []
    for j in range(i, len(substrings)-1):
      substrings_next = substrings[0:j]+[substrings[j]+substrings[j+1]]+substrings[j+2:]
      if is_palindrome(substrings_next[j]):
        res.append(substrings_next)
        res.extend(partition_helper(substrings_next, j))
      elif j < len(substrings_next)-1:
        substrings_next_2 = substrings_next
        for _ in range(j, len(substrings_next_2)-1):
          substrings_next_2 = substrings_next_2[0:j]+[substrings_next_2[j]+substrings_next_2[j+1]]+substrings_next_2[j+2:]
          if is_palindrome(substrings_next_2[j]):
            res.append(substrings_next_2)
            res.extend(partition_helper(substrings_next_2, j))
            break
    return res
      
  return [list(s)] + partition_helper(list(s), 0)

def partition2(s):
  def is_palindrome(s):
    return s==s[::-1]

  seeds = [(list(s), 0)]
  res = [seeds[0][0]]
  while len(seeds)>0:
    substrings, i = seeds.pop()
    for j in range(i, len(substrings)-1):
      substrings_next = substrings[0:j]+[substrings[j]+substrings[j+1]]+substrings[j+2:]
      if is_palindrome(substrings_next[j]):
        res.append(substrings_next)
        seeds.append((substrings_next, j))
      elif j < len(substrings_next)-1:
        substrings_next_2 = substrings_next
        for _ in range(j, len(substrings_next_2)-1):
          substrings_next_2 = substrings_next_2[0:j]+[substrings_next_2[j]+substrings_next_2[j+1]]+substrings_next_2[j+2:]
          if is_palindrome(substrings_next_2[j]):
            res.append(substrings_next_2)
            seeds.append((substrings_next_2, j))
            break
          
  return res


# testing
test_cases = [('aab', [['a', 'a', 'b'], ['aa', 'b']]),
              ('a', [['a']]),
              ('abbab', [['a', 'b', 'b', 'a', 'b'], ['abba', 'b'], ['a', 'bb', 'a', 'b'], ['a', 'b', 'bab']])]

for case, ans in test_cases:
  res = partition2(case)
  if res==ans:
    print('PASS')
  else:
    print('FAIL')

# performance analysis
from timeit import timeit
print("Partition1 timeit results:")
for _ in range(5):
  print(timeit(lambda: (partition1(case) for case in test_cases), number=int(1e3)))
print("Partition2 timeit results:")
for _ in range(5):
  print(timeit(lambda: (partition1(case) for case in test_cases), number=int(1e3)))