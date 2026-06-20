from typing import List

# https://leetcode.com/problems/maximum-building-height/


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        heights = [(1, 0)]
        heights.extend(sorted(restrictions))
        heights.append((n, 1 << 31))

        edit_q = list(range(len(heights)))
        q_elements = set(range(len(heights)))
        while edit_q:
            i = edit_q.pop()
            q_elements.remove(i)
            x, h = heights[i]

            for j in [i - 1, i + 1]:
                if j < 0 or j >= len(heights):
                    continue
                xj, hj = heights[j]

                h_new = h + abs(x - xj)
                if h_new < hj:
                    heights[j] = (xj, h_new)
                    if j not in q_elements:
                        edit_q.append(j)
                        q_elements.add(j)
        # print(heights)

        best = 0
        for i in range(1, len(heights)):
            xl, hl = heights[i - 1]
            xr, hr = heights[i]
            h_mid = (xr - xl + hl + hr) // 2
            best = max(best, hl, hr, h_mid)

        return best
