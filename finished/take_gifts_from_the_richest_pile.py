import heapq
import math
from typing import List

# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        g = [-n for n in gifts]
        heapq.heapify(g)

        for _ in range(k):
          n = heapq.heappop(g)
          heapq.heappush(g, -math.floor(math.sqrt(-n)))
        
        return -sum(g)