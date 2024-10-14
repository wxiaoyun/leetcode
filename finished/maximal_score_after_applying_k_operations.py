import heapq
import math
from typing import List

# https://leetcode.com/problems/maximal-score-after-applying-k-operations

# Time: O(n + klogn)
# Space: O(n)
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums] # O(n)
        heapq.heapify(max_heap) # O(n)

        score = 0
        for _ in range(k): # k iterations, O(klogn)
          n = -1* heapq.heappop(max_heap) # n is negative, O(logn)
          score += n
          heapq.heappush(max_heap, -math.ceil(n/3)) # O(logn)
        return score
