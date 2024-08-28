# https://leetcode.com/problems/n-ary-tree-postorder-traversal/


# Definition for a Node.
from typing import List, Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
      res = []

      def helper(node: Optional[Node]) -> None:
        if not node:
          return None
        
        for n in node.children:
          helper(n)
        
        res.append(node.val)
        return None
      
      helper(root)
      return res
        