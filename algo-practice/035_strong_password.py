def minimumNumber(n, password):
  numbers = "0123456789"
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  special_characters = "!@#$%^&*()-+"
  test_num = False
  test_lower = False
  test_upper = False
  test_special = False
  for char in password:
    if not test_num and char in numbers:
      test_num = True
    if not test_lower and char in lower_case:
      test_lower = True
    if not test_upper and char in upper_case:
      test_upper = True
    if not test_special and char in special_characters:
      test_special = True
  pass_total = sum([test_num, test_lower, test_upper, test_special])
  fail_total = 4-pass_total
  return max(6-n, fail_total)

test_case = (5, '2bbbb')
print(minimumNumber(*test_case))