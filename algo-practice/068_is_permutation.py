def is_permutation(str_1, str_2):
  if sorted(list(str_1))==sorted(list(str_2)):
    return True
  return False

print(is_permutation('asdf', 'fdsa')) # True
print(is_permutation('asdc', 'fdsa')) # False