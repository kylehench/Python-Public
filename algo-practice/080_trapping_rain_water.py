# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
  def trap(self, height: List[int]) -> int:
    if len(height) <= 2:
      return 0
    maximum = 0
    max_left = [0]
    for i in range(len(height)-1):
      maximum = max(maximum, height[i])
      max_left.append(maximum)
    
    maximum = 0
    max_right = [0]
    for i in range(len(height)-1, 0, -1):
      maximum = max(maximum, height[i])
      max_right.append(maximum)
    max_right.reverse()
    
    vol = 0
    for i in range(1, len(height)-1):
      vol += max(0, min(max_left[i], max_right[i])-height[i])
    return vol