# https://leetcode.com/problems/balance-a-binary-search-tree

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def linearize(n: TreeNode, output: List[int]) -> None:
    if not n:
        return
    
    linearize(n.left, output)
    output.append(n.val)
    linearize(n.right, output)

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        linearize(root, arr)

        def gen_bst(l:int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            if l == r:
                return TreeNode(val=arr[l])

            m = l + (r-l)//2
            return TreeNode(
                val = arr[m],
                left = gen_bst(l, m-1),
                right = gen_bst(m+1, r)
            )

        return gen_bst(0, len(arr)-1)