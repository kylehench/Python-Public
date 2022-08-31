# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

class Solution:
  def countAndSay(self, n: int) -> str:
    def recursive(n):
      if n==1:
        return '1'
      inner_res = recursive(n-1)
      res = ''
      ch1 = inner_res[0]
      count = 1
      for ch in inner_res[1:]:
        if ch1==ch:
          count += 1
        else:
          res += (str(count) + ch1)
          ch1 = ch
          count = 1

      res += (str(count) + ch1)
      return res
    return recursive(n)