def anagram(s):
  if len(s)%2 != 0:
    return -1
  a = [ch for ch in s[:int(len(s)/2)]]
  b = [ch for ch in s[int(len(s)/2):]]
  common = 0
  for ch in a:
    if ch in b:
      b.remove(ch)
    else:
      common += 1
  return common



test_cases = ('abc','mnop','xyyx')
for case in test_cases:
  print(anagram(case))