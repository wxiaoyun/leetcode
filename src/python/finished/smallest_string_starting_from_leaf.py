from typing import Optional, List

# https://leetcode.com/problems/smallest-string-starting-from-leaf/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        best = None

        def dfs(node: Optional[TreeNode], chrs: List[str] = []) -> None:
            if node is None:
                return None
            chrs.append(chr(node.val + ord("a")))

            if node.left is None and node.right is None:
                nonlocal best
                s = "".join(reversed(chrs))
                if best is None or s < best:
                    best = s

            dfs(node.left, chrs)
            dfs(node.right, chrs)

            chrs.pop()
            return None

        dfs(root)
        return best or ""
