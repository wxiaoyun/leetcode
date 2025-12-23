from typing import List

# https://neetcode.io/problems/meeting-schedule


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ints = [(i.start, i.end) for i in intervals]
        ints.sort()

        for i in range(1, len(ints)):
            ps, pe = ints[i - 1]
            s, e = ints[i]

            if pe > s:
                return False
        return True
