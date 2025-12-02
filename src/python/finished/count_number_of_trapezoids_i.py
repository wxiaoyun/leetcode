from typing import List
from collections import defaultdict

# O(n) where n is the number of points
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        level_cnt = defaultdict(int)
        for _, y in points:
            level_cnt[y] += 1

        MOD = int(1e9) + 7
        total = 0
        prev_candidates = 0
        for points in level_cnt.values():
            local_candidates = points * (points - 1) // 2
            total = (total + prev_candidates * local_candidates) % MOD
            prev_candidates += local_candidates
        return total


# TLE: O(n + k^2) where n is the number of points and k is the number of levels
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        level_cnt = defaultdict(int)

        for x, y in points:
            level_cnt[y] += 1

        # for every 2 level
        # (level_i choose 2) * (level_j choose 2)
        MOD = int(1e9) + 7
        total = 0

        levels = list(level_cnt.keys())
        l = len(levels)
        for i in range(l):
            i_cnt = level_cnt[levels[i]]
            i_choices = i_cnt * (i_cnt - 1) // 2

            for j in range(i + 1, l):
                j_cnt = level_cnt[levels[j]]
                j_choices = j_cnt * (j_cnt - 1) // 2

                total = (total + i_choices * j_choices) % MOD

        return total