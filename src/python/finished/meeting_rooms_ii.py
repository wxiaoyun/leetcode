import heapq
from typing import List

# https://neetcode.io/problems/meeting-schedule-ii/


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        ints = [(i.start, i.end) for i in intervals]
        ints.sort()

        days = [-1]
        for s, e in ints:
            if days[0] > s:
                heapq.heappush(days, e)
                continue

            heapq.heappop(days)
            heapq.heappush(days, e)

        return len(days)
