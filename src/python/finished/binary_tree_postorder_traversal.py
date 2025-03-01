# https://leetcode.com/problems/binary-tree-postorder-traversal/description/


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Post order: Left, right, root
        order = []

        def helper(node: Optional[TreeNode]) -> None:
            if not node:
                return None
            
            helper(node.left)
            helper(node.right)
            order.append(node.val)
            return None
        
        helper(root)
        return order