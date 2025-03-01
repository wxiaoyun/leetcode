# https://leetcode.com/problems/create-binary-tree-from-descriptions


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {} # Dict[int, TreeNode]
        parent = {} # Dict[int, int]

        for p, c, left in descriptions:
            if p not in nodes:
                pnode = TreeNode(p)
                nodes[p] = pnode
            else:
                pnode = nodes[p]
            
            if c not in nodes:
                cnode = TreeNode(c)
                nodes[c] = cnode
            else:
                cnode = nodes[c]
            
            if left == 1:
                pnode.left = cnode
            else:
                pnode.right = cnode
            
            parent[c] = p
        

        cur = descriptions[0][0]
        while cur in parent:
            cur = parent[cur]
        
        return nodes[cur]