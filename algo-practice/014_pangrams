# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.

def pangrams(s):
  letters = {chr(int_char) : False for int_char in range(ord('a'),ord('z')+1)}
  for char in s:
    letters[char.lower()] = True
  if False in letters.values():
    return 'not pangram'
  else:
    return 'pangram'

if __name__ == '__main__':

  l = ['We promptly judged antique ivory buckles for the next prize', 'We promptly judged antique ivory buckles for the prize']

  for s in l:
    print(pangrams(s))
