import heapq
from typing import List

# https://leetcode.com/problems/two-best-non-overlapping-events/


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events = [(s, e, v) for s, e, v in events]
        events.sort()

        best = 0
        best_left = 0
        pq = []
        for s, e, v in events:
            while pq and pq[0][0] < s:
                _, prev_v = heapq.heappop(pq)
                best_left = max(best_left, prev_v)

            best = max(best, v, best_left + v)
            heapq.heappush(pq, (e, v))

        return best


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()  # sort by start time in ascending order
        v_best = 0
        pqe = []  # min heap by end time: Pq<Tuple<end, value>>
        best = -1

        for s, e, v in events:
            # retrieve all events whose ending time is before the start of the current event
            while pqe and pqe[0][0] < s:
                _, v_other = heapq.heappop(pqe)
                # update best value so far
                v_best = max(v_best, v_other)

            best = max(best, v + v_best)

            # push the current event to the endtime min heap
            heapq.heappush(pqe, (e, v))

        return best

