# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque()
        dq.append((0, root))
        output = []

        while len(dq) > 0:
            (l, n) = dq.popleft()

            if n == None:
                continue
            
            while len(output) <= l:
                output.append([])

            dq.append((l+1, n.left))
            dq.append((l+1, n.right))
            output[l].append(n.val)
        
        return output
