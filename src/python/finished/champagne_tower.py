# https://leetcode.com/problems/champagne-tower/


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # P1: F
        # P2: F | 1/2, 1/2
        # P3: F | F, F
        # P4: F | F, F | 1/4, 1/2, 1/4
        # P5: F | F, F | 1/2, F, 1/2
        # P6: F | F, F | 3/4, F, 3/4 | 0, 1/4, 1/4, 0

        # query(i, j) is equivalent to
        # max(0, query(i - 1, j - 1) - 1) + max(0, query(i - 1, j) - 1)

        def inflow(dp: dict, i: int, j: int) -> float:
            if i < 0 or j > i:
                return 0.0

            if i == 0 and j == 0:
                return poured

            key = (i, j)
            if key in dp:
                return dp[key]

            left_inflow, right_inflow = inflow(dp, i - 1, j - 1), inflow(dp, i - 1, j)
            left_outflow, right_outflow = (
                max(0, left_inflow - 1),
                max(0, right_inflow - 1),
            )
            cur_inflow = left_outflow / 2 + right_outflow / 2

            dp[key] = cur_inflow
            return cur_inflow

        return min(1, inflow({}, query_row, query_glass))
