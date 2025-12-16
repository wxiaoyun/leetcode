from typing import List

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        def compute(dp: dict, r: int, c: int) -> int:
            key = (r, c)
            if key in dp:
                return dp[key]

            best = 1
            val = matrix[r][c]
            for rr, cc in [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]:
                if min(rr, cc) < 0 or rr >= m or cc >= n:
                    continue

                if matrix[rr][cc] <= val:
                    continue

                best = max(best, 1 + compute(dp, rr, cc))

            dp[key] = best
            return best

        dp = {}
        best = 0
        for r in range(m):
            for c in range(n):
                best = max(best, compute(dp, r, c))
        return best
