from typing import List

# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        prev_s, prev_e = intervals[0]
        for s, e in intervals:
            if prev_e >= s:
                prev_e = max(prev_e, e)
                continue

            res.append([prev_s, prev_e])
            prev_s, prev_e = s, e

        res.append([prev_s, prev_e])
        return res
