from typing import Optional, Tuple

# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node: TreeNode) -> Tuple[int, int]:
            mp = node.val
            msp = node.val

            NEG_INF = -float("inf")

            lmp, lmsp = helper(node.left) if node.left else (NEG_INF, NEG_INF)
            rmp, rmsp = helper(node.right) if node.right else (NEG_INF, NEG_INF)

            if node.left:
                mp = max(mp, lmp)
                msp = max(msp, lmsp + node.val)

            if node.right:
                mp = max(mp, rmp)
                msp = max(msp, rmsp + node.val)

            if node.left and node.right:
                mp = max(mp, lmsp + rmsp + node.val)

            mp = max(mp, msp)

            return mp, msp

        return helper(root)[0]
