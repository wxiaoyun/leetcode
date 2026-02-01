import heapq
from typing import List

# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        pq = []
        for n in nums[1:]:
            heapq.heappush(pq, -n)
            if len(pq) > 2:
                heapq.heappop(pq)

        return nums[0] - sum(pq)
