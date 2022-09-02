# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    def recursive(temp_list, pool):
      for i in range(len(pool)):
        num = pool[i]
        next_pool = pool.copy()
        del next_pool[i]
        if len(next_pool)>0:
          recursive([item + [num] for item in temp_list], next_pool)
        else:
          res.extend([item + [num] for item in temp_list])
    recursive([[]], nums)
    return res