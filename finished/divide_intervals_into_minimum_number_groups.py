import heapq
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        groups = 1
        pq = [intervals[0][1]] # priority queue for the group with the earliest end time
        for st, et in intervals[1:]:
          earliest_et = pq[0]
          if earliest_et < st:
            heapq.heappop(pq)
            heapq.heappush(pq, et)
          else:
            groups += 1
            heapq.heappush(pq, et)
        return groups


# class Solution:
#     def minGroups(self, intervals: List[List[int]]) -> int:
#         intervals = sorted(intervals)

#         groups = [intervals[0][1]] # list of ending time for each group
#         for interval in intervals[1:]:
#           st, et = interval
#           # Try to find an existing group that can accommodate the interval
#           idx = None
#           for i, ett in enumerate(groups):
#             if ett < st:
#               if not idx:
#                 idx = i
#               else:
#                 idx = idx if groups[idx] < ett else i
          
#           if idx == None:
#             groups.append(et)
#           else:
#             groups[idx] = et

#         return len(groups)