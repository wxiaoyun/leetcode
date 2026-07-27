import heapq
from typing import List

# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) > 2:
                heapq.heappop(pq)
        return (pq[0] - 1) * (pq[1] - 1)
