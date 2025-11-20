from typing import List

# https://leetcode.com/problems/set-intersection-size-at-least-two


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda p: (p[1], -p[0]))

        n_picked = 0
        picked_n_1, picked_n_2 = -1, -1
        for l, r in intervals:
            if l > picked_n_2:
                picked_n_1, picked_n_2 = r - 1, r
                n_picked += 2
            elif l > picked_n_1:
                picked_n_1, picked_n_2 = picked_n_2, r
                n_picked += 1
        return n_picked
