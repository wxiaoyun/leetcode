# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(lst: List[int], node: TreeNode) -> None:
            if node.left is not None:
                helper(lst, node.left)
            lst.append(node.val)
            if node.right is not None:
                helper(lst, node.right)
            return None

        ret = []
        if root is not None:
            helper(ret, root)
        return ret
