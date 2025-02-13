import heapq
from typing import List

# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq = nums
        heapq.heapify(pq)
        op = 0

        while len(pq) > 1:
            a = heapq.heappop(pq)
            if a >= k:
                break

            b = heapq.heappop(pq)
            heapq.heappush(pq, a * 2 + b)
            op += 1
        
        return op
            
