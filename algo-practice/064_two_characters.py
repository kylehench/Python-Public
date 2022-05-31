# Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters.
# Example
# s = 'abaacdabd'
# Delete a, to leave bcdbd. Now, remove the character c to leave the valid string bdbd with a length of 4. Removing either b or d at any point would not result in a valid string. Return 4.
# Given a string s, convert it to the longest possible string t made up only of alternating characters. Return the length of string t. If no string t can be formed, return 0.

def alternate(s):
  # list of unique letters
  char_list = list(set(s))
  longest_solution = 0
  # loop through unordered combinations of letters
  for i, a in enumerate(char_list):
    for b in char_list[i+1:]:
      # test string containing only two letters
      test = [ch for ch in s if ch==a or ch==b]
      # check if two letters alternate
      if all(x!=y for x, y in zip(test[:-1], test[1:])) and len(test) > longest_solution:
        longest_solution = len(test)
  return longest_solution

test_cases = ('abaacdabd','beabeefeab',) # 4, 5
for case in test_cases:
  print(alternate(case))