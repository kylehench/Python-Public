# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []
    res = []
    current_nodes = [root]
    while len(current_nodes) > 0:
      res.append([node.val for node in current_nodes])
      next_nodes = []
      for node in current_nodes:
        if node.left:
          next_nodes.append(node.left)
        if node.right:
          next_nodes.append(node.right)
      current_nodes = next_nodes
    return res