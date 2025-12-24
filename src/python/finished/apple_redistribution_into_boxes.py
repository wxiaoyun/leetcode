import heapq
from typing import List

# https://leetcode.com/problems/apple-redistribution-into-boxes


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n_apple = sum(apple)
        n_cap = len(capacity)

        heapq.heapify_max(capacity)
        while capacity and n_apple > 0:
            n_apple -= heapq.heappop_max(capacity)

        return n_cap - len(capacity)
