# https://leetcode.com/problems/maximum-number-of-points-with-cost/

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # DP
        # Time O(m*n^2)
        # Space O(n)
        # M = len(points)
        # N = len(points[0])
        # max_to_prev_row = [0] * N

        # for r in range(M):
        #   max_to_cur_row = [-float('inf')] * N
        #   for c_target in range(N):
        #     for c in range(N):
        #       max_to_cur_row[c_target] = max(
        #         max_to_cur_row[c_target],
        #         max_to_prev_row[c] + points[r][c] - abs(c_target - c)
        #       )
        #   max_to_prev_row = max_to_cur_row

        # return max(max_to_prev_row)

        # DP Optimized
        # Time O(m*n)
        # Space O(n)
        M = len(points)
        N = len(points[0])
        max_to_prev_row = [0] * N

        for i in range(M):
          prefix_max = [None] * N
          postfix_max = [None] * N

          for l in range(N):
            prefix_max[l] = max(
              max_to_prev_row[l] + points[i][l],
              prefix_max[l-1] - 1 if l > 0 else -float('inf')
            )
            r = N-l-1
            postfix_max[r] = max(
              max_to_prev_row[r] + points[i][r],
              postfix_max[r+1] - 1 if r < N-1 else -float('inf')
            )
          
          for c in range(N):
            max_to_prev_row[c] = max(
              prefix_max[c],
              postfix_max[c]
            )

        return max(max_to_prev_row)

