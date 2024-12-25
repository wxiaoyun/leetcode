from collections import deque
from typing import Optional

# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        level_vals = []
        q = deque([root])

        while q:
            llen = len(q)
            vals = []
            for _ in range(llen):
                n = q.popleft()

                vals.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            level_vals.append(vals)

        def swaps(arr):
            index = {v: i for i, v in enumerate(arr)}
            srt = sorted(arr)

            swaps = 0
            for i, v in enumerate(srt):
                if srt[i] == arr[i]:
                    continue

                swaps += 1

                a_i = i
                a_v = arr[i]

                b_i = index[v]
                b_v = v

                arr[a_i], arr[b_i] = arr[b_i], arr[a_i]
                index[a_v], index[b_v] = index[b_v], index[a_v]
            return swaps

        return sum([swaps(arr) for arr in level_vals])

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = [[root.val]]

        cur_node_level = [root]
        while cur_node_level:
            next_node_level = []
            next_val_level = []

            for n in cur_node_level:
                if n.left:
                    next_node_level.append(n.left)
                    next_val_level.append(n.left.val)
                if n.right:
                    next_node_level.append(n.right)
                    next_val_level.append(n.right.val)

            levels.append(next_val_level)
            cur_node_level = next_node_level

        def get_min_swaps(arr) -> int:
            target = sorted(arr)

            pos = {v: i for i, v in enumerate(arr)}
            swaps = 0
            for i, v in enumerate(arr):
                if v != target[i]:
                    swaps += 1

                    p = pos[target[i]]
                    pos[v] = p
                    arr[p] = arr[i]
            return swaps

        return sum([get_min_swaps(arr) for arr in levels])
