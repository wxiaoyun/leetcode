# Definition for a binary tree node.
import heapq
from typing import Dict, List, Optional

# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        level_heights = [] #List[MinHeap[Tuple[height, node_val]]]
        node_to_level: Dict[int, int] = {}  # Dict[node_val, level]

        def height_helper(node: TreeNode, level: int = 0) -> int:
          if not node:
            return -1

          node_to_level[node.val] = level

          height = 1 + max(
            height_helper(node.left, level+1), 
            height_helper(node.right, level+1)
          )

          while level >= len(level_heights):
            level_heights.append([])
          heapq.heappush(level_heights[level], (height + level, node.val))
          while len(level_heights[level]) > 2:
            heapq.heappop(level_heights[level])

          return height

        height_helper(root) # O(n)

        result = [-1] * len(queries)
        for idx, q in enumerate(queries): # O(q) iterations
          level = node_to_level[q] # O(1)
          heights = level_heights[level] # O(1)

          if len(heights) == 1 and heights[0][1] == q:
            result[idx] = level - 1 # O(1)
          elif heights[1][1] == q:
            result[idx] = heights[0][0] # O(1)
          else:
            result[idx] = heights[1][0] # O(1)
        return result