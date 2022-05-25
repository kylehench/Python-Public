# Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.

# Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String

def superReducedString(s):
  s = list(s)
  while 1:
    i = 0
    complete = True
    while i<len(s)-1:
      if s[i]==s[i+1]:
        s[i], s[i+1] = 0, 0
        complete = False
        i += 1
      i += 1
    s = [ch for ch in s if ch != 0]
    if complete == True:
      break
  if len(s)==0 or (len(s)==2 and s[0]==s[1]):
    return 'Empty String'
  return ''.join(s)

test_cases = ('aab','abba','aa')
for case in test_cases:
  print(superReducedString(case))