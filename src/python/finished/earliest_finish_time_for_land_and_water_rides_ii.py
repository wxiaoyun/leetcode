import heapq
from typing import List

# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        lst = landStartTime
        ld = landDuration
        wst = waterStartTime
        wd = waterDuration
        n, m = len(lst), len(wst)

        lands = set((lst[i], ld[i]) for i in range(n))
        waters = set((wst[j], wd[j]) for j in range(m))

        LAND, WATER = 1 << 0, 1 << 1
        DONE = LAND | WATER
        pq = [(0, 0)]
        while pq:
            t, state = heapq.heappop(pq)
            if state == DONE:
                return t

            if state & LAND == 0:
                for st, d in lands:
                    start = max(t, st)
                    heapq.heappush(pq, (start + d, state | LAND))

            if state & WATER == 0:
                for st, d in waters:
                    start = max(t, st)
                    heapq.heappush(pq, (start + d, state | WATER))

        return -1
