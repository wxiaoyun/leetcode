from typing import Optional

# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # find the deepest nodes
        # track their parents
        # go up level by level there we find a single common ancestor
        if root is None:
            return None

        parent_of = {}
        q = [root]
        while q:
            cur_lvl = []

            for n in q:
                if n.left:
                    parent_of[n.left] = n
                    cur_lvl.append(n.left)
                if n.right:
                    parent_of[n.right] = n
                    cur_lvl.append(n.right)

            if not cur_lvl:
                break

            q = cur_lvl

        cur = set(q)
        while len(cur) > 1:
            parent = set()

            for n in cur:
                parent.add(parent_of[n])

            cur = parent

        return cur.pop()
