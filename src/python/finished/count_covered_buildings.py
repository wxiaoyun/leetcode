from collections import defaultdict
from typing import List

# https://leetcode.com/problems/count-covered-buildings/


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        N = len(buildings)
        buildings = sorted(buildings)
        buildings_cover = [0] * len(buildings)

        top_cover = defaultdict(bool)
        left_cover = False
        cur_row = 0
        for i, (r, c) in enumerate(buildings):
            if r != cur_row:
                cur_row = r
                left_cover = False

            if left_cover:
                buildings_cover[i] += 1
            left_cover = True

            if top_cover[c]:
                buildings_cover[i] += 1
            top_cover[c] = True

        bot_cover = defaultdict(bool)
        right_cover = False
        cur_row = -1
        for i in reversed(range(N)):
            r, c = buildings[i]

            if r != cur_row:
                cur_row = r
                right_cover = False

            if right_cover:
                buildings_cover[i] += 1
            right_cover = True

            if bot_cover[c]:
                buildings_cover[i] += 1
            bot_cover[c] = True

        return sum(1 if c == 4 else 0 for c in buildings_cover)
