from typing import Optional


# https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def mirror_compare(left, right) -> bool:
            if left == right:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return mirror_compare(left.left, right.right) and mirror_compare(
                left.right, right.left
            )

        return mirror_compare(root.left, root.right)
