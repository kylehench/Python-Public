# Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
# Check if the given string is a correct variable name.

def solution(name):
  if name[0].isdigit():
    return False
  for ch in name:
    if not (ch.isalnum() or ch == '_'):
      return False
  return True