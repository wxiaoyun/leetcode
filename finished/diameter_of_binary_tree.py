# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0
        def max_depth(node):
            nonlocal max_diam
            if node == None:
                return 0

            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)
            max_diam = max(max_diam, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        max_depth(root)
        return max_diam
        

        