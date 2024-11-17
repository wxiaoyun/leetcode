import heapq
from typing import List

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # O(nlogn)
        best = float('inf')
        total = 0
        pq = []

        for i, num in enumerate(nums):
          total += num

          if total >= k:
            best = min(best, i+1)
          
          while pq and (total - pq[0][0]) >= k:
            _, j = heapq.heappop(pq)
            best = min(best, i-j)
          
          heapq.heappush(pq, (total, i))

        return best if best != float('inf') else -1

    # def shortestSubarray(self, nums: List[int], k: int) -> int:
    #     # O(n^2)
    #     n = len(nums)
    #     best = float('inf')

    #     for i in range(n):
    #       accum = 0
    #       for j in range(i, n):
    #         accum += nums[j]
    #         if accum >= k:
    #           best = min(best, j - i + 1)
    #           break
    #     return best if best != float('inf') else -1