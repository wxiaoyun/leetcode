from collections import deque
from typing import Optional

# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level_sum = -float("inf")
        max_lvl = -1

        lvl = -1
        q = deque([root])
        while q:
            lvl += 1
            level_sum = 0

            l = len(q)
            for _ in range(l):
                n = q.popleft()
                level_sum += n.val

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_lvl = lvl

        return max_lvl + 1
