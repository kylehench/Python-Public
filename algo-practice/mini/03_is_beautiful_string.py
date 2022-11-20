# A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.
# Given a string, check whether it is beautiful.

def solution(inputString):
  letters = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
  for ch in inputString:
    letters[ch] += 1
  letters_list = list(letters.items())
  letters_list.sort()
  for i in range(len(letters_list)-1):
    if letters_list[i][1] < letters_list[i+1][1]:
      return False
  return True