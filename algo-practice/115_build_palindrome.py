# Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

def solution(st):
  test = st
  while not all(test[i]==test[-1-i] for i in range(int(len(test)/2))):
    test = test[1:]
  return st + st[:len(st)-len(test)][::-1]
        