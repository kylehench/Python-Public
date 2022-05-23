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
  # incomplete
  fowards = s[0:int(len(s)/2)]
  backwards = s[int(len(s)/2)-(len(s)+1)%2+1:][::-1]
  print(fowards, backwards)

test_cases = ('aaab','baa','aaa')
for case in test_cases:
  print(palindromeIndex2(case))