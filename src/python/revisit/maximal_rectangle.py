from typing import List

# https://leetcode.com/problems/maximal-rectangle/


# O(mn)
# Build histogram and reduce problem to maximal rectangle of histogram
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        C = len(matrix[0])

        max_area = 0
        hist = [0] * (C + 1)
        for row in matrix:
            for i, bit in enumerate(row):
                if bit == "1":
                    hist[i] += 1
                else:
                    hist[i] = 0

            # left, shortest column
            stack = []
            for r, h in enumerate(hist):
                while stack and h < hist[stack[-1]]:
                    l = stack.pop()
                    height = hist[l]
                    width = r - (stack[-1] + 1 if stack else 0)
                    max_area = max(max_area, height * width)
                stack.append(r)

        return max_area
