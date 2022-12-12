# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def grow_branch(node, nums):
      i_mid = len(nums)//2
      node.val = nums[i_mid]
      if len(nums)>1:
        node.left = TreeNode()
        grow_branch(node.left, nums[0:i_mid])
      if len(nums)>2:
        node.right = TreeNode()
        grow_branch(node.right, nums[i_mid+1:])
    root = TreeNode()
    grow_branch(root, nums)
    return root