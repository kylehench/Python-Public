# Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

def isValid(s):
  letters = {}
  for ch in s:
    if ch in letters:
      letters[ch] += 1
    else:
      letters[ch] = 1
  counts = {}
  for value in letters.values():
    if value in counts:
      counts[value] += 1
    else:
      counts[value] = 1
  counts_reversed = {value:key for key, value in counts.items()}
  if len(counts)==1: return 'YES'
  elif len(counts)==2:
    minority_letters_count = min(counts.values())
    majority_letters_count = max(counts.values())
    if minority_letters_count!=1: return 'NO'
    if counts_reversed[minority_letters_count]-counts_reversed[majority_letters_count]==1 or counts_reversed[minority_letters_count]==1:
      return 'YES'
    return 'NO'
  else: return 'NO'


test_cases = (
  ('abcc','YES'),
  ('aabbccd','YES'),
  ('abccc','NO'),
  ('aabbcd','NO'),
  ('aabbccddeefghi','NO'),
  ('abcdefghhgfedecba','YES'),
)
for s, expected in test_cases:
  print('PASS') if isValid(s) == expected else print('FAIL')