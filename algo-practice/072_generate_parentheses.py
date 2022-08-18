# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses

class Solution1:
  def generateParenthesis(self, n: int) -> List[str]:
    res = set(['()'])
    for _ in range(n-1):
      new_res = []
      for string in res:
        new_res += [string[:i] + '()' + string[i:] for i in range(len(string)+1)]
      res = set(new_res)
    return list(res)

class Solution2:
  def generateParenthesis(self, n: int) -> List[str]:
    res = []
    def build(string, open_n, closed_n):
      if open_n == closed_n == n:
        res.append(string)
        return
      if open_n < n:
        build(string + '(', open_n+1, closed_n)
      if closed_n < open_n:
        build(string + ')', open_n, closed_n+1)
    build('', 0, 0)
    return res