from collections import defaultdict, deque
from typing import Optional

# https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      level_sum = []
      parent_sum = defaultdict(int)

      queue = deque([(None, root)])
      while queue:
        size = len(queue)
        sm = 0
        for _ in range(size):
          parent, node = queue.popleft()

          if not node:
            continue
          
          sm += node.val
          parent_sum[parent] += node.val
          queue.append((node, node.left))
          queue.append((node, node.right))

        level_sum.append(sm)
      
      queue = deque([(None, root)])
      lv= 0
      while queue:
        size = len(queue)
        for _ in range(size):
          parent, node = queue.popleft()

          if not node:
            continue
          
          node.val = level_sum[lv] - parent_sum[parent]
          queue.append((node, node.left))
          queue.append((node, node.right))
        lv += 1
      
      return root