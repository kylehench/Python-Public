def palindromeIndex1(s):
  # incomplete
  if s==s[::-1]:
    return -1
  length = len(s)
  for i in range(length):
    test = s[0:i] + s[i+1:length]
    if test==test[::-1]:
      return i
  return -1

def palindromeIndex2(s):
  fowards = s[0:int(len(s)/2)]
  backwards = s[int(len(s)/2)-(len(s)+1)%2+1:][::-1]
  for i, (a, b) in enumerate(zip(fowards, backwards)):
    if a==b:
      continue
    else:
      s_test = list(s)
      del s_test[i]
      if s_test[0:int(len(s_test)/2)] == s_test[int(len(s_test)/2)-(len(s_test)+1)%2+1:][::-1]:
        return i
      s_test = list(s)
      del s_test[len(s_test)-1-i]
      if s_test[0:int(len(s_test)/2)] == s_test[int(len(s_test)/2)-(len(s_test)+1)%2+1:][::-1]:
        return len(s_test)-i
  return -1

test_cases = ('aaab','baa','aaa')
for case in test_cases:
  print(palindromeIndex2(case))