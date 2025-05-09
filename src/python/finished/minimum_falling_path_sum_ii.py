from typing import List
import heapq

# https://leetcode.com/problems/minimum-falling-path-sum-ii


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        dp = grid[0][:]

        for r in range(1, R):
            pq = []
            for i, n in enumerate(dp):
                heapq.heappush(pq, (-n, i))
                if len(pq) > 2:
                    heapq.heappop(pq)

            for c in range(C):
                if pq[1][1] == c:
                    dp[c] = grid[r][c] - pq[0][0]
                else:
                    dp[c] = grid[r][c] - pq[1][0]

        return min(dp)
