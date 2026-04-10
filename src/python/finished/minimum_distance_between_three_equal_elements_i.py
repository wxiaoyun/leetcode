from collections import defaultdict
from typing import List

# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        for i, n in enumerate(nums):
            indices[n].append(i)

        INF = 1 << 32
        ans = INF
        for ls in indices.values():
            if len(ls) < 3:
                continue

            for idx in range(len(ls) - 2):
                i, j, k = ls[idx : idx + 3]
                ans = min(ans, abs(i - j) + abs(j - k) + abs(k - i))

        return ans if ans < INF else -1
