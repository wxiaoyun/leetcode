from typing import List, Optional

# https://leetcode.com/problems/balance-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        node_vals = []
        stack = [root]
        while stack:
            n = stack.pop()
            if isinstance(n, int):
                node_vals.append(n)
                continue

            if n.right:
                stack.append(n.right)
            stack.append(n.val)
            if n.left:
                stack.append(n.left)

        def build_node(arr: List[int], l: int, r: int) -> Optional[TreeNode]:
            if l >= r:
                return None

            m = l + (r - l) // 2
            return TreeNode(arr[m], build_node(arr, l, m), build_node(arr, m + 1, r))

        return build_node(node_vals, 0, len(node_vals))
