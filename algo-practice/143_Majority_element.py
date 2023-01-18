# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(self, nums: List[int]) -> int:
  if len(nums)==1:
    return nums[0]
  count = {}
  majority_threshold = len(nums)/2
  for num in nums:
    if num in count:
      count[num] += 1
      if count[num] > majority_threshold:
        return num
    else:
      count[num] = 1