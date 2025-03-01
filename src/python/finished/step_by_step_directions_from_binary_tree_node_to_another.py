# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ReverseNode:
    def __init__(self, parent=None, this=None, dir=None):
        self.parent = parent
        self.this = this
        self.dir = dir

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lookup = {
            root.val: ReverseNode(this=root)
        }

        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return

            left = node.left
            if left:
                lookup[left.val] = ReverseNode(parent=lookup[node.val], this=left, dir="L")
                traverse(node.left)

            right= node.right
            if right:
                lookup[right.val] = ReverseNode(parent=lookup[node.val], this=right, dir="R")
                traverse(node.right)


        traverse(root)

        path_start = [] # from start node to root
        cur = lookup[startValue] # ReverseNode
        while cur:
            path_start.append(cur)
            cur = cur.parent

        start_set = set(path_start)
        common_parent = None

        path_dest = [] # from dest node to first common ancestor
        cur = lookup[destValue]
        while cur:
            path_dest.append(cur)
            if cur in start_set:
                common_parent = cur
                break
            cur = cur.parent

        if not common_parent:
            raise Exception("No common parent found")        

        path = []
        for rn in path_start:
            if rn == common_parent:
                break
            path.append("U")
        for rn in reversed(path_dest[:-1]):
            path.append(rn.dir)

        return "".join(path)