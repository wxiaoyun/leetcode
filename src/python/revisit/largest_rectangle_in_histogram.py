from typing import List

# https://leetcode.com/problems/largest-rectangle-in-histogram/


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # area of rec = height * base
        # we cannot form a rect if it is concave

        heights.append(-1)
        stk = []

        best = 0
        for i in range(len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                l = stk.pop()
                h = heights[l]
                w = i if not stk else i - stk[-1] - 1
                best = max(best, w * h)
            stk.append(i)

        return best
