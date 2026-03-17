from typing import List

# https://leetcode.com/problems/largest-submatrix-with-rearrangements/


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        ans = 0
        histogram = [0] * n
        for row in matrix:
            for i, d in enumerate(row):
                histogram[i] = 0 if d == 0 else 1 + histogram[i]

            heights = sorted(histogram[:])
            ans = max(ans, max(h * (n - i) for i, h in enumerate(heights)))

        return ans
