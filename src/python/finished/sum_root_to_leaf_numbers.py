from typing import Optional

# https://leetcode.com/problems/sum-root-to-leaf-numbers/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode], prefix: int = 0) -> int:
        new_prefix = prefix * 10 + root.val
        if root.left is None and root.right is None:
            return new_prefix

        sums = 0
        if root.left is not None:
            sums += self.sumNumbers(root.left, new_prefix)
        if root.right is not None:
            sums += self.sumNumbers(root.right, new_prefix)
        return sums
