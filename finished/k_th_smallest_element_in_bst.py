# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.count = 0

        def dfs_in_order(n: Optional[TreeNode], k: int):
            if not n or self.res:
                return
            
            dfs_in_order(n.left, k)
            self.count += 1

            if self.count == k:
                self.res = n.val
            
            dfs_in_order(n.right, k)
            
        dfs_in_order(root, k)
        
        return self.res
