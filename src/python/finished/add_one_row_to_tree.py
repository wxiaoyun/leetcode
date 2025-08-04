# https://leetcode.com/problems/add-one-row-to-tree/


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        def dfs(
            node: Optional[TreeNode], val: int, target_depth: int, depth: int
        ) -> Optional[TreeNode]:
            if node is None:
                return node

            if depth != target_depth - 1:
                dfs(node.left, val, target_depth, depth + 1)
                dfs(node.right, val, target_depth, depth + 1)
                return node

            # depth == target_depth - 1
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
            return node

        dummy = TreeNode(-1, left=root)
        dfs(dummy, val, depth, 0)
        return dummy.left
