import heapq
from typing import List

# https://leetcode.com/problems/last-stone-weight/


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            z = (-y) - (-x)
            if z != 0:
                heapq.heappush(stones, -z)

        return -stones[0] if stones else 0
