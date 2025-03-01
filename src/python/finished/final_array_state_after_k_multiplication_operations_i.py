import heapq
from typing import List

# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
      pq = [(n, i) for i, n in enumerate(nums)]
      heapq.heapify(pq)

      for _ in range(k):
        n, i = heapq.heappop(pq)
        nk = n * multiplier
        heapq.heappush(pq, (nk, i))
        nums[i] = nk
      
      return nums
        