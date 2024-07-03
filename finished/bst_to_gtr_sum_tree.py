# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumMut(n: TreeNode, extra: Optional[int] = None) -> int:
    if not n:
        return 0
    rsum = sumMut(n.right, extra)
    val = n.val
    n.val += rsum
    n.val += extra if extra else 0
    lsum = sumMut(n.left, n.val)
    return lsum + val + rsum

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sumMut(root, None)
        return root