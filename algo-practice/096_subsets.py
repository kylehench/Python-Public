# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution1:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    def extend(arr, elements):
      if len(elements)==0:
        return arr
      next_el = elements.pop()
      arr.extend([item + [next_el] for item in arr])
      return extend(arr, elements)
    return extend([[]], nums)

class Solution2:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = [[]]
    for num in nums:
      res.extend([item + [num] for item in res])
    return res