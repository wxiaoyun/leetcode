import heapq
from typing import List

# https://leetcode.com/problems/non-overlapping-intervals/


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        best_non_overlapping = 0
        best_left = 0
        pq = []
        for s, e in intervals:
            while pq and pq[0][0] <= s:
                _, cnt = heapq.heappop(pq)
                best_left = max(best_left, cnt)

            best_non_overlapping = max(best_non_overlapping, best_left + 1)
            heapq.heappush(pq, (e, best_left + 1))

        return len(intervals) - best_non_overlapping
