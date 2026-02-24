from typing import Optional

# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(node: Optional[TreeNode], accum: int = 0) -> int:
            if node is None:
                return 0
            accum = (accum << 1) + node.val
            if node.left is None and node.right is None:
                return accum
            return helper(node.left, accum) + helper(node.right, accum)

        return helper(root)
