# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     return self.isValidBSTUtil(root, -sys.maxsize, sys.maxsize)
    # 
    # def isValidBSTUtil(self, node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
    #     if node is None:
    #         return True
    #     
    #     if node.val <= min_val or node.val >= max_val:
    #         return False
    #     
    #     left_valid = self.isValidBSTUtil(node.left, min_val, node.val)
    #     right_valid = self.isValidBSTUtil(node.right, node.val, max_val)
    #     
    #     return left_valid and right_valid
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_bound(node: TreeNode, low: int, high: int) -> bool:
            if node == None:
                return True
            
            if not (node.val < high and node.val > low):
                return False
            
            return (
                check_bound(node.left, low, node.val) and
                check_bound(node.right, node.val, high)
            )
        
        return check_bound(root, -float('inf'), float('inf'))
