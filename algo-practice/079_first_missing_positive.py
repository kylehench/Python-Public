# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    nums_set = set(nums)
    num = 1
    while num in nums_set:
      num +=1
    return num  