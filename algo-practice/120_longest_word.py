# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

def solution(text):
  i_long, j_long = 0, 0
  i, j = 0, 0
  active = False
  for idx, ch in enumerate(text):
    if not active:
      if ch.isalpha():
        i = idx
        active = True
    if active:
      if not ch.isalpha():
        j = idx
        active = False
        if j-i > j_long-i_long:
          i_long, j_long = i, j
  if active:
    j = len(text)
    if j-i > j_long-i_long:
      i_long, j_long = i, j
  return text[i_long:j_long]