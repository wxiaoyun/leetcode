from typing import Optional, Tuple

# https://leetcode.com/problems/balanced-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode]) -> Tuple[bool, int]:
            if node is None:
                return True, 0

            left_balance, left_depth = helper(node.left)
            right_balance, right_depth = helper(node.right)

            return left_balance and right_balance and abs(
                left_depth - right_depth
            ) <= 1, max(left_depth, right_depth) + 1

        return helper(root)[0]


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node == None:
                return 0

            left_height = helper(node.left)
            right_height = helper(node.right)

            if left_height < 0 or right_height < 0:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        result = helper(root)
        return False if result < 0 else True
