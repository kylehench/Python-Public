# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

class Solution:
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
      return
    level = [root]
    while level[0].left:
      level_next = []
      for node in level:
        level_next.extend([node.left, node.right])
      for i in range(len(level_next)-1):
        level_next[i].next = level_next[i+1]
      level = level_next
    return root