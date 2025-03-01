from collections import defaultdict
import heapq
from typing import List

# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

class Solution:
    def findScore(self, nums: List[int]) -> int:
        left_of = defaultdict(lambda: None)
        right_of = defaultdict(lambda: None)
        pq = []

        for i, n in enumerate(nums):
          node = (n, i)
          pq.append(node)
          if i > 0:
            right_of[i-1] = node
          if i < len(nums) - 1:
            left_of[i+1] = node
        
        heapq.heapify(pq)
        score = 0
        marked = set()
        while pq:
          node = heapq.heappop(pq)
          n, i = node

          if node in marked:
            continue

          score += n

          for n in [left_of[i], node, right_of[i]]:
            if n:
              marked.add(n)
        
        return score
