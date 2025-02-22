import re
from typing import Optional

#  https://leetcode.com/problems/recover-a-tree-from-preorder-traversal

 # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        pattern = r"([-]*\d+)"
        matches = re.finditer(pattern, traversal)

        stack = []
        for m in matches:
            part = m.group(1)
            depth, num = 0, 0
            for i, ch in enumerate(part):
                if ch == "-":
                    continue

                depth = i
                num = int(part[i:])
                break
            
            if depth == 0:
                stack.append((depth, TreeNode(num)))
                continue
            
            prev_depth, _ = stack[-1]
            pops = prev_depth - depth + 1

            for _ in range(pops):
                stack.pop()
            
            node = TreeNode(num)
            _, pnode = stack[-1]
            if not pnode.left:
                pnode.left = node
            else:
                pnode.right = node
            stack.append((depth, node))

        return stack[0][1]


            