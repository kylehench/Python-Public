# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    res = [0] + digits
    increment_map = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:0}
    digit = len(res) - 1
    while digit >= 0:
      res[digit] = increment_map[res[digit]]
      if res[digit] != 0:
        break
      digit -= 1
    if res[0] == 0:
      del res[0]
    return res