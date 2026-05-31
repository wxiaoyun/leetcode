import heapq
from typing import List

# https://leetcode.com/problems/destroying-asteroids


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        pq = []
        for am in asteroids:
            if am <= mass:
                # print(mass, am)
                mass += am
            else:
                heapq.heappush(pq, am)

            while pq and pq[0] <= mass:
                # print(mass, pq[0])
                mass += heapq.heappop(pq)

        # print(pq)
        return len(pq) == 0
