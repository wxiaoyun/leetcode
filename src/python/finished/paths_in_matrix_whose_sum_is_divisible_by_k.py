from typing import List

# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # a % k + b % k = 0 % k
        # a and b must be complements

        # Define: ways(src_r, src_c, dest_r, dest_c, l) -> int
        # The number ways to traverse from (src_r, src_c) to (dest_r, dest_c), modulo k equals l
        #
        # Given a path that crosses (i, j)
        # the number of paths that is divisble by k is given by:
        # Sum l in 0..k:
        #   ways(0, 0, i, j, l) * ways(i, j, m - 1, n - 1, k - l)

        MOD = int(1e9 + 7)
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * k for _ in range(n)]
        dp[-1][0] = 1

        for r in reversed(range(m)):
            new_dp = [[0] * k for _ in range(n)]

            for c in reversed(range(n)):
                cell_val = grid[r][c]

                for l in range(k):
                    new_l = (cell_val + l) % k

                    # update from prev_row
                    new_dp[c][new_l] += dp[c][l]
                    new_dp[c][new_l] %= MOD

                    # update from prev_col
                    new_dp[c][new_l] += new_dp[c + 1][l] if c + 1 < n else 0
                    new_dp[c][new_l] %= MOD

            dp = new_dp

        return dp[0][0]
