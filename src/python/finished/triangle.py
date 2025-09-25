from typing import List

# https://leetcode.com/problems/triangle/


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_min = [0]

        for row in triangle:
            cur_min = [float("inf")] * len(row)

            for i, n in enumerate(row):
                local_min = float("inf")

                if i < len(prev_min):
                    local_min = min(local_min, prev_min[i] + n)

                if i - 1 >= 0:
                    local_min = min(local_min, prev_min[i - 1] + n)

                cur_min[i] = local_min

            prev_min = cur_min

        return min(prev_min)
