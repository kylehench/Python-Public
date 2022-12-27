# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if len(nums)==0:
      return 0
    nums.sort()
    length = 1
    length_max = 1
    for i in range(1, len(nums)):
      if nums[i] == nums[i-1]+1:
        length += 1
        if length > length_max:
          length_max = length
      elif nums[i] == nums[i-1]:
        pass
      else:
        length = 1
    return length_max