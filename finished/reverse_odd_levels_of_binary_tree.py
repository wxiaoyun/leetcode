from typing import Optional

# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = []
        cur = [root]

        while cur:
          llen = len(cur)
          next_lvl = []

          for i in range(llen):
            n = cur[i]
            if n.left:
              next_lvl.append(n.left)
              next_lvl.append(n.right) # tree is perfect
          
          levels.append(cur)
          cur = next_lvl

        for i, l in enumerate(levels):
          if i % 2 == 1:
            l.reverse()
        
        for l in range(len(levels)-1):
          next_lvl = levels[l+1]

          for i, n in enumerate(levels[l]):
            i_left = (i * 2)
            i_right = (i * 2 + 1)
            n.left = next_lvl[i_left]
            n.right = next_lvl[i_right]
            
        return root
