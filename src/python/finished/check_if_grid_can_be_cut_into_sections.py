from typing import List

# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/?envType=daily-question&envId=2025-03-25


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_split(intervals: list[list[int]]) -> bool:
            intervals = sorted(intervals)

            splits = 0
            prev_s, prev_e = intervals[0][0], intervals[0][1]

            for s, e in intervals[1:]:
                if s < prev_e:
                    prev_e = max(prev_e, e)
                    continue

                splits += 1
                if splits >= 3:
                    return True

                prev_s, prev_e = s, e

            splits += 1
            return splits >= 3

        hori_intervals = [(s, e) for s, _, e, _ in rectangles]
        vert_intervals = [(s, e) for _, s, _, e in rectangles]
        return can_split(hori_intervals) or can_split(vert_intervals)
