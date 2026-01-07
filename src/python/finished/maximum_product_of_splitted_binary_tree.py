from typing import Optional

# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree_total = 0
        stack = [root]
        while stack:
            n = stack.pop()
            if not n:
                continue
            tree_total += n.val
            stack.append(n.left)
            stack.append(n.right)

        best_prod = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_sub_total = dfs(node.left)
            left_prod = left_sub_total * (tree_total - left_sub_total)
            right_sub_total = dfs(node.right)
            right_prod = right_sub_total * (tree_total - right_sub_total)

            nonlocal best_prod
            best_prod = max(best_prod, left_prod, right_prod)

            return node.val + left_sub_total + right_sub_total

        dfs(root)
        MOD = int(1e9) + 7
        return best_prod % MOD
