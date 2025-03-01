from typing import List, Optional

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Cursor:
    def __init__(self, arr):
        self.arr = arr
        self.i = 0
    
    def has_next(self) -> bool:
        return self.i < len(self.arr)
    
    def peek(self):
        return self.arr[self.i]
    
    def advance(self):
        self.i += 1
    
    def next(self):
        if not self.has_next():
            return None
        item = self.peek()
        self.advance()
        return item

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def construct(precursor: Cursor, postcursor: Cursor) -> Optional[TreeNode]:
            if not precursor.has_next():
                return None
            
            preval = precursor.next()
            tn = TreeNode(preval)
            
            if preval == postcursor.peek():
                postcursor.advance()
                return tn
            
            tn.left = construct(precursor, postcursor)
            if preval == postcursor.peek():
                postcursor.advance()
                return tn

            tn.right = construct(precursor, postcursor)
            if preval == postcursor.peek():
                postcursor.advance()
            return tn
        
        return construct(Cursor(preorder), Cursor(postorder))

