# CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

# Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

def solution(inputString):
  count = 0
  num_str = ''
  i = 0
  while i < len(inputString):
    if inputString[i].isnumeric():
      while i < len(inputString) and inputString[i].isnumeric():
        num_str += inputString[i]
        i += 1
      count += int(num_str)
      num_str = ''
    i += 1
  return count