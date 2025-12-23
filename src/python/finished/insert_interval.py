from typing import List

# https://leetcode.com/problems/insert-interval/


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        s, e = newInterval

        # binary search for the smallest index j such that s <= intervals[j][0]
        idx = len(intervals)
        l, r = 0, len(intervals)
        while l < r:
            m = l + (r - l) // 2
            if intervals[m][0] <= s:
                # l.......m...s..r
                l = m + 1
            else:
                idx = m
                r = m

        res = []

        prev_s, prev_e = intervals[0] if intervals and idx != 0 else newInterval
        for i in range(len(intervals) + 1):
            if i == idx:
                if prev_e >= s:
                    prev_e = max(prev_e, e)
                else:
                    res.append([prev_s, prev_e])
                    prev_s, prev_e = s, e

            if i < len(intervals):
                ss, ee = intervals[i]
                if prev_e >= ss:
                    prev_e = max(prev_e, ee)
                    continue

                res.append([prev_s, prev_e])
                prev_s, prev_e = ss, ee

        res.append([prev_s, prev_e])

        return res
