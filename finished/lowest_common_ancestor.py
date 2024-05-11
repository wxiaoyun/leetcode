# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def trace_find(current: 'TreeNode', target: 'TreeNode', arr: List['TreeNode']=[]) -> List['TreeNode']:
            arr.append(current)

            if current.val == target.val:
                return arr

            if current.val > target.val:
                # Search left subtree
                return trace_find(current.left, target, arr)
            else:
                return trace_find(current.right, target, arr)

        p_trace = trace_find(root, p, [])
        q_trace = trace_find(root, q, [])

        i = 0
        while True:
            if i >= len(p_trace) or i >= len(q_trace):
                return p_trace[i-1]

            if p_trace[i].val != q_trace[i].val:
                return p_trace[i-1]
            
            i += 1
