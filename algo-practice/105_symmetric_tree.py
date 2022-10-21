# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root.left and not root.right:
      return True
    if (root.left==None) ^ (root.right==None):
      return False

    def check(left, right):

      if left.val != right.val:
        return False

      if (left.left==None) ^ (right.right==None):
        return False
      if left.left and right.right and check(left.left, right.right)==False:
        return False

      if (left.right==None) ^ (right.left==None):
        return False
      if left.right and right.left and check(left.right, right.left)==False:
        return False

      return True

    return check(root.left, root.right)