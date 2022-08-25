class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    # special cases
    if len(nums)==0: return [-1, -1]
    if len(nums)==1:
      if nums[0] != target: return [-1, -1]
      else: return [0, 0]
    
    # find start position
    if nums[0] == target:
      start = 0
    else:
      def find_start(start, end):
        if nums[start]==target and nums[start-1] != target: return start
        if nums[end]==target and nums[end-1] != target: return end
        if end-start <= 1: return -1
        mid_idx = int((start+end)/2)
        if nums[mid_idx] < target:
          return find_start(mid_idx+1, end-1)
        else:
          return find_start(start+1, mid_idx)
      start = find_start(0, len(nums)-1)
        
    # find end position
    if start == -1:
      return [-1, -1]
    if nums[-1] == target:
      end = len(nums)-1
    else:
      def find_end(start, end):
        if nums[start]==target and nums[start+1] != target: return start
        if nums[end]==target and nums[end+1] != target: return end
        if end-start <= 1: return -1
        mid_idx = int((start+end)/2)
        if nums[mid_idx] > target:
          return find_end(start+1, mid_idx-1)
        else:
          return find_end(mid_idx, end-1)
              
      end = find_end(start, len(nums)-2)
    return([start, end])