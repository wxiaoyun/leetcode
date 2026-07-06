from typing import List

# https://leetcode.com/problems/remove-covered-intervals/


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda l: (l[0], -l[1]))
        print(intervals)

        n_covered = 0
        n = len(intervals)
        i, j = 0, 0
        while True:
            i = j
            if i >= n:
                break
            a, b = intervals[i]

            j = i + 1
            while j < n:
                c, d = intervals[j]

                if not b >= d:
                    break
                n_covered += 1

                j += 1

        return n - n_covered
