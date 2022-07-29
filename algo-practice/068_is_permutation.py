def is_permutation(str_1, str_2):
  if sorted(str_1)==sorted(str_2):
    return True
  return False

print(is_permutation('asdf', 'fdsa')) # True
print(is_permutation('asdc', 'fdsa')) # False