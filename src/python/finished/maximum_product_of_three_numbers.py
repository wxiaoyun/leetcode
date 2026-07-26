import heapq
from typing import List

# https://leetcode.com/problems/maximum-product-of-three-numbers/


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pos_pq = []
        neg_pq = []
        neg_min_pq = []

        for n in nums:
            if n >= 0:
                heapq.heappush(pos_pq, n)
            else:
                heapq.heappush(neg_pq, -n)
                heapq.heappush(neg_min_pq, n)

            if len(pos_pq) > 3:
                heapq.heappop(pos_pq)
            if len(neg_pq) > 2:
                heapq.heappop(neg_pq)
            if len(neg_min_pq) > 3:
                heapq.heappop(neg_min_pq)

        # print(pos_pq)
        # print(neg_pq)

        best = -(1 << 64)
        if len(pos_pq) >= 3:
            best = max(best, pos_pq[0] * pos_pq[1] * pos_pq[2])
        if len(pos_pq) and len(neg_pq) >= 2:
            best = max(best, max(pos_pq) * neg_pq[0] * neg_pq[1])
        if len(neg_min_pq) >= 3:
            best = max(best, neg_min_pq[0] * neg_min_pq[1] * neg_min_pq[2])
        return best
