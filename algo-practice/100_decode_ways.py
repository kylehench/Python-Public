class Solution:
  def numDecodings(self, s: str) -> int:
    def count(i):
      res = 0
      if i >= len(s) or s[i]=='0':
        return 0
      
      if i==len(s)-1:
        return 1
      
      res += count(i+1)
      
      if int(s[i:i+2])<=26:
        if i==len(s)-2:
          res += 1
        else:
          res += count(i+2)
      return res
      

    return count(0)