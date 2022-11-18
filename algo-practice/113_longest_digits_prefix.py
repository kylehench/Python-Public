# Given a string, output its longest prefix which contains only digits.

def solution(inputString):
  i = 0
  while i < len(inputString):
    if inputString[i].isdigit():
      i += 1
    else:
      break
  return inputString[0:i]