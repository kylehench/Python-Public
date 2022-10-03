# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    i = 0
    summation = 0
    min_length = 10**6
    for j in range(len(nums)):
      num = nums[j]
      summation += num
      while summation - nums[i] >= target:
        summation -= nums[i]
        i += 1
      if summation >= target and j-i+1 < min_length:
        min_length = j-i+1
    if min_length == 10**6:
      return 0
    else:
      return min_length