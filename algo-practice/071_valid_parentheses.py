class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{',  ']': '['}
    for ch in s:
      if ch not in pairs:
        stack.append(ch)
      elif len(stack)>0 and stack.pop()==pairs[ch]:
        pass
      else:
        return False
    if len(stack)==0:
      return True
    else:
      return False