# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.

import math
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

import sys

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTUtil(root, -sys.maxsize, sys.maxsize)
    
    def isValidBSTUtil(self, node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        if node is None:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        left_valid = self.isValidBSTUtil(node.left, min_val, node.val)
        right_valid = self.isValidBSTUtil(node.right, node.val, max_val)
        
        return left_valid and right_valid
