# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate1(self, nums: List[int], k: int) -> None:
  length = len(nums)
  nums_next = [nums[(i-k)%length] for i in range(length)]
  for i in range(length):
    nums[i] = nums_next[i]

def rotate2(self, nums: List[int], k: int) -> None:
  k %= len(nums)
  def reverse_in_place(arr, i_start, i_end):
    for i in range((i_end-i_start+1)//2):
        arr[i_start+i], arr[i_end-i] = arr[i_end-i], arr[i_start+i]
  # reverse whole array
  reverse_in_place(nums, 0, len(nums)-1)
  # reverse starting segment
  reverse_in_place(nums, 0, k-1)
  # reverse ending segment
  reverse_in_place(nums, k, len(nums)-1)