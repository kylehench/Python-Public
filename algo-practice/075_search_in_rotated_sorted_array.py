class Solution:
  def search(self, nums: List[int], target: int) -> int:
    # check if first value == target. If not and len(nums)==1, return -1
    if nums[0]==target: return 0
    if len(nums)==1:
      return -1
    
    threshold = nums[0]
    def search(i_min, i_max):
      if nums[i_min]==target: return i_min
      if nums[i_max]==target: return i_max
      if i_max-i_min<=1:
        return -1
      i_center = int((i_min+i_max)/2)
      if target > nums[i_center]:
        return search(i_center, i_max)
      else:
        return search(i_min, i_center)
        
    # if numns is not rotated, binary search array
    if nums[-1] > nums[0]:
      return search(1, len(nums)-1)
    else:
      # numns is rotated. Find pivot with binary search and search appropriate range that possibly contains target, and return result.
      def find_pivot(i_min, i_max):
        if nums[i_max]<nums[i_max-1]: return i_max
        if nums[i_min]<nums[i_min-1]: return i_min
        if i_max-i_min<=1:
          return -1
        i_center = int((i_min+i_max)/2)
        if nums[i_center]<nums[0]:
          return find_pivot(i_min, i_center)
        else:
          return find_pivot(i_center, i_max)
      i_rotate = find_pivot(1, len(nums)-1)
      if target > nums[0]:
        return search(1, i_rotate-1)
      else:
        return search(i_rotate, len(nums)-1)