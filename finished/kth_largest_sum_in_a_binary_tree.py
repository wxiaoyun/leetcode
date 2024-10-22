from collections import defaultdict
from typing import Optional

# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sum = defaultdict(int)

        def helper(node: TreeNode, l: int) -> None:
          if not node:
            return None
          
          level_sum[l] += node.val
          helper(node.left, l+1)
          helper(node.right, l+1)
          return None
        
        helper(root, 0)
        
        if len(level_sum) < k:
          return -1

        level_sum = [(val, l) for l, val in level_sum.items()]
        level_sum.sort(reverse=True)
        return level_sum[k-1][0]