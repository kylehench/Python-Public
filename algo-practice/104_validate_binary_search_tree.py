# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
    
class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def check(node, left, right):
      if node.left:
        if not (left < node.left.val < node.val):
          return False
        if not check(node.left, left, node.val):
          return False
        
      if node.right:
        if not (node.val < node.right.val < right):
          return False
        if not check(node.right, node.val, right):
          return False
      
      return True
    
    return check(root, float('-inf'), float('inf'))