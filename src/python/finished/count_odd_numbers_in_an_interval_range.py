# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 0 -> 0
        # 1 -> 1
        # 2 -> 1
        # 3 -> 2
        # 4 -> 2

        high_cnt = (high + 1) // 2
        low_cnt = (low - 1 + 1) // 2
        return high_cnt - low_cnt
