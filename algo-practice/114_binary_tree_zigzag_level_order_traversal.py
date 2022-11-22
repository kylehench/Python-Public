# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    nodes = [root]
    res = []
    if not root:
      return res
    reverse = False
    
    while len(nodes)>0:
      next_nodes = []
      new_level = []
      for node in nodes:
        new_level.append(node.val)
        if node.left:
          next_nodes.append(node.left)
        if node.right:
          next_nodes.append(node.right)
      
      if reverse:
        new_level.reverse()
      res.append(new_level)
      nodes = next_nodes
      reverse = not reverse
    return res