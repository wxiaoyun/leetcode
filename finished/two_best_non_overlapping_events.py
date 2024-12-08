import heapq
from typing import List

# https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort() # sort by start time in ascending order
        v_best = 0
        pqe = [] # min heap by end time: Pq<Tuple<end, value>>
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

    # def maxTwoEvents(self, events: List[List[int]]) -> int:
    #     pq = [(-v, s, e) for (s, e, v) in events]
    #     heapq.heapify(pq)

    #     best = -1
    #     for a_start, a_end, a_value in events:
    #       best = max(best, a_value)

    #       pqq = copy.deepcopy(pq)
    #       while pqq:
    #         v, s, e = heapq.heappop(pqq)
    #         if s > a_end or e < a_start:
    #           # print(a_start, a_end, s, e)
    #           best = max(best, a_value - v)
    #           break
    #     return best
