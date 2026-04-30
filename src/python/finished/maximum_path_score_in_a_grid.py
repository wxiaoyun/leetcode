from typing import List

# https://leetcode.com/problems/maximum-path-score-in-a-grid/


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        INF = 1 << 32
        dp = [[-INF] * (k + 1) for _ in range(n)]
        dp[0][0] = 0
        for i in range(m):
            tmp = [[-INF] * (k + 1) for _ in range(n)]
            for j in range(n):
                v, c = grid[i][j], min(1, grid[i][j])

                for kk in range(k + 1):
                    if kk - c < 0:
                        continue
                    tmp[j][kk] = dp[j][kk - c] + v

                    if j > 0:
                        tmp[j][kk] = max(tmp[j][kk], tmp[j - 1][kk - c] + v)
            dp = tmp
            # print(dp)

        best = max(dp[-1])
        return best if best >= 0 else -1
