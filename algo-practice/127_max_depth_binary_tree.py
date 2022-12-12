# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    def descend(node, depth):
      if not node.left and not node.right:
        return depth
      if node.left:
        depth_left = descend(node.left, depth+1)
      else:
        depth_left = depth
      if node.right:
        depth_right = descend(node.right, depth+1)
      else:
        depth_right = depth
      return max(depth_left, depth_right)
    return descend(root, 1)