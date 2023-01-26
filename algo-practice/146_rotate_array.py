# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(self, nums: List[int], k: int) -> None:
  length = len(nums)
  nums_next = [nums[(i-k)%length] for i in range(length)]
  for i in range(length):
    nums[i] = nums_next[i]