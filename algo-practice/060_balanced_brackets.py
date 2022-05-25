def isBalanced(s):
  length = len(s)
  if length%2 != 0:
    return 'NO'
  pairs = {'[':']','{':'}','(':')',}
  pairs_reverse = {value:key for key, value in pairs.items()}
  open = set(pairs.keys())

  que = [0 for _ in range(length)]
  i = 0
  for ch in s:
    if ch in open:
      que[i] = ch
      i += 1
    else:
      if que[i-1] != pairs_reverse[ch]:
        return 'NO'
      i -= 1
  return 'NO' if i!=0 else 'YES'

test_cases = ('{[()]}','{[(])}','{{[[(())]]}}')
for case in test_cases:
  print(isBalanced(case))