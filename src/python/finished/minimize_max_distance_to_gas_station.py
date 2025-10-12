import math
from typing import List
import heapq

# https://leetcode.com/problems/minimize-maximum-distance-to-gas-station/


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(penalty: float) -> bool:
            k_rem = k
            for i in range(1, len(stations)):
                finish = stations[i]
                start = stations[i - 1]
                dist = finish - start

                cities_needed = math.ceil(dist / penalty) - 1
                k_rem -= cities_needed

                if k_rem < 0:
                    return False

            return True

        prev_penalty = -1
        l, r = 0, -1
        for i in range(1, len(stations)):
            dist = stations[i] - stations[i - 1]
            r = max(r, dist)
            prev_penalty = r

        eps = 1e-6
        while True:
            m = l + (r - l) / 2

            if possible(m):
                if abs(prev_penalty - m) < eps:
                    return m
                prev_penalty = m
                r = m
            else:
                l = m

        return -1


# TLE, time O(N + klogN)
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        adj_distances = []
        for i in range(1, len(stations)):
            finish = stations[i]
            start = stations[i - 1]
            adj_distances.append((start - finish, finish, start, 1))
        heapq.heapify(adj_distances)

        for _ in range(k):
            _, finish, start, n = heapq.heappop(adj_distances)
            heapq.heappush(
                adj_distances, ((start - finish) / (n + 1), finish, start, n + 1)
            )
        return -adj_distances[0][0]
