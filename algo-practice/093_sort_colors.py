# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # find index of first non-zero value
        for not_0_idx in range(len(nums)):
            if nums[not_0_idx] != 0:
                break
        # swap non-zero values at front of list with 0 values in middle
        for i in range(not_0_idx+1, len(nums)):
            if nums[i] == 0:
                nums[not_0_idx], nums[i] = nums[i], nums[not_0_idx]
                not_0_idx += 1
        
        # find last non-2 value in list
        for not_2_idx in range(len(nums)-1, -1, -1):
            if nums[not_2_idx] != 2:
                break
        # swap non-2 values at back of list with 2 values in middle
        for i in range(not_2_idx-1, -1, -1):
            if nums[i] == 2:
                nums[not_2_idx], nums[i] = nums[i], nums[not_2_idx]
                not_2_idx -= 1
        return nums