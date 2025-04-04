from collections import deque
from typing import Optional

# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parent = {root.val: -1}
        q = deque([root])
        lowest = []
        while q:
            llen = len(q)
            lowest = list(q)

            for _ in range(llen):
                n = q.popleft()

                if n.left:
                    parent[n.left.val] = n
                    q.append(n.left)

                if n.right:
                    parent[n.right.val] = n
                    q.append(n.right)

        low_len = len(lowest)
        if low_len == 1:
            return lowest[0]

        p_same = False
        p = None
        while not p_same:
            p_same = True
            for i in range(1, low_len):
                n = lowest[i]
                prev = lowest[i - 1]

                p_same = p_same and (parent[n.val] == parent[prev.val])

                lowest[i - 1] = parent[prev.val]

            lowest[-1] = parent[lowest[-1].val]

            if p_same:
                p = lowest[0]
                break

        return p
