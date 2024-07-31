# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs

from collections import defaultdict
from typing import Dict, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if distance < 2:
            return 0
        
        # Return the number of good pairs in n and a dictionary of distances between n and its leafs and the corresponding number of leaf nodes 
        def helper(n: TreeNode) -> Tuple[int, Dict[int, int]]:
            if not n:
                return (0, {})
            
            # leaf node
            if not n.left and not n.right:
                return (0, {0: 1})
            
            lcount, ldict = helper(n.left)
            rcount, rdict = helper(n.right)

            new_dict = defaultdict(int)

            ldict_items = []
            for l, c in ldict.items():
                new_dict[l+1] += c
                ldict_items.append((l, c))
            ldict_items.sort()

            rdict_items = []
            for l, c in rdict.items():
                new_dict[l+1] += c
                rdict_items.append((l, c))
            rdict_items.sort()

            total_count = lcount + rcount
            for llen, lcnt in ldict_items:
                for rlen, rcnt in rdict_items:
                    if llen+rlen+2 > distance:
                        break # break inner loop
                    total_count += lcnt*rcnt
            
            return total_count, new_dict
        
        return helper(root)[0]