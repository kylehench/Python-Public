# A numeric string, s, is beautiful if it can be split into a sequence of two or more positive integers that satisfyi the following conditions:
# (1) a[i] - a[i-1] = 1
# (2) No leading zeroes
# (3) s contents cannot be rearranged

def separateNumbers(s):
  def match(i, s):
    if len(s)==0:
      return True
    if len(str(i)) > len(s) or str(i) != s[:len(str(i))]:
      return False
    return match(i+1, s[len(str(i)):])

  seed_len_max = len(s)//2
  for seed_len in range(1, seed_len_max+1):
    i = int(s[:seed_len])
    if match(i+1, s[len(str(i)):]) == True:
      print('YES ' + str(i))
      return None
  print('NO')
  return None

test_cases = ('1234','91011','99100','10203','1234','91011','99100','101103','010203','13','1','99910001001','7891011','9899100','999100010001')
for test_case in test_cases:
  print('Test case: ' + test_case)
  separateNumbers(test_case)