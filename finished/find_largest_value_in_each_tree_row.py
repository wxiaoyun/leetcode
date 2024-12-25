from collections import deque
from typing import List, Optional

# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        level = deque()
        if root:
          level.append(root)

        while level:
          llen = len(level)
          mx = -float('inf')

          for _ in range(llen):
            n = level.popleft()

            mx = max(mx, n.val)

            if n.left:
              level.append(n.left)
            if n.right:
              level.append(n.right)

          res.append(mx)
        
        return res