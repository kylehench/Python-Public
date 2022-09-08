# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
      if num > current_sum and current_sum < 0:
        current_sum = num
      else:
        current_sum += num
      if current_sum > max_sum:
        max_sum = current_sum
    return max_sum