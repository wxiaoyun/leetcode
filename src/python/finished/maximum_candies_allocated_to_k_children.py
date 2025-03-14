from typing import List

# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/?envType=daily-question&envId=2025-03-14


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(v: int) -> bool:
            if v == 0:
                return True

            count = 0
            for c in candies:
                count += c // v
            return count >= k

        l, r = 0, max(candies) + 1

        while l < r:
            m = l + (r - l) // 2

            if not possible(m):
                r = m
            else:
                l = m + 1

        return l - 1
