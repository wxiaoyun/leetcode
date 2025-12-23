import heapq
from typing import List

from sortedcontainers import SortedList

# https://leetcode.com/problems/minimum-interval-to-include-each-query/


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # I need a data structure that stores an ordered list of intervals
        # 1. Intervals should be ordered based on size
        # 2. I also need an efficient way to delete intervals based on end index

        intervals.sort()
        query_indices = [(q, i) for i, q in enumerate(queries)]
        query_indices.sort()

        # PriorityQueue<(end_index, index)>
        del_queue = []
        size_index = SortedList(key=lambda i: intervals[i][1] - intervals[i][0])

        i = 0
        ans = [-1] * len(queries)
        for q, k in query_indices:
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(del_queue, (e, i))
                size_index.add(i)
                i += 1

            while del_queue and del_queue[0][0] < q:
                _, j = heapq.heappop(del_queue)
                size_index.remove(j)

            if size_index:
                j = size_index[0]
                ans[k] = intervals[j][1] - intervals[j][0] + 1

        return ans
