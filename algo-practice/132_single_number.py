# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    find_one = set()
    for num in nums:
      if num in find_one:
        find_one.remove(num)
      else:
        find_one.add(num)
    return list(find_one)[0]