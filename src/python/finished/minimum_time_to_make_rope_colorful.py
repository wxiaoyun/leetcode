from typing import List

# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        n = len(colors)
        i = 0
        while i < n:
            c = colors[i]
            count = 0
            local_total = 0
            max_t = -1
            while i < n and colors[i] == c:
                count += 1
                t = neededTime[i]
                local_total += t
                max_t = max(t, max_t)
                i += 1

            if count > 1:
                total += local_total - max_t

        return total
