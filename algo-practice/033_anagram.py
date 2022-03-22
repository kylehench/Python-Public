from timeit import timeit

def anagram(s):
  if len(s)%2 != 0:
    return -1
  a = [ch for ch in s[:int(len(s)/2)]]
  b = [ch for ch in s[int(len(s)/2):]]
  uncommon = 0
  for ch in a:
    if ch in b:
      b.remove(ch)
    else:
      uncommon += 1
  return uncommon

def anagram1(s):
  if len(s)%2 != 0:
    return -1
  b = {}
  for ch in s[int(len(s)/2):]:
    if ch in b:
      b[ch] += 1
    else:
      b[ch] = 1
  uncommon = 0
  for ch in s[:int(len(s)/2)]:
    if ch in b:
      if b[ch] == 1:
        del b[ch]
      else:
        b[ch] -= 1
    else:
      uncommon += 1
  return uncommon

test_cases = ('abc','mnop','xyyx','mnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxnrkrokbjtnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmnopxyyxmpxyyx')
def test():
  for case in test_cases:
    anagram(case)
def test1():
  for case in test_cases:
    anagram1(case)

print(timeit(lambda: test(), number=1000))
print(timeit(lambda: test1(), number=1000))