def is_unique(str):
  newSet = set()
  for ch in str:
    if ch in newSet:
      return False
    newSet.add(ch)
  return True

print(is_unique('asdf'))   # True
print(is_unique('asdfa'))  # False