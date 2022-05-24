def sherlockAndAnagrams(s):
  pairs = 0
  for length in range(1,len(s)):
    hashes={}
    for i in range(len(s)+1-length):
      hash1 = hash(str(sorted(s[i:i+length])))
      if hash1 in hashes:
        hashes[hash1] += 1
      else:
        hashes[hash1] = 1
    for count in hashes.values():
      if count > 1:
        pairs += sum(i for i in range(count))
  return pairs


test_cases = ('mom','ifailuhkqq','cdcd')
for case in test_cases:
  print(sherlockAndAnagrams(case))