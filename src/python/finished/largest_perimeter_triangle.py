from typing import List

# https://leetcode.com/problems/largest-perimeter-triangle/


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)

        # Three sides of a triangle: a, b, c
        # Suppose a is the longest side.
        # then: a < b + c <= 2a

        # We can sort all lengths and loop from the back (start with the longest)
        # n_1, ..., n_k-2, n_k-1, n_k

        # Observation:
        # 1. n_k is guaranteed to be the largest: n_k-2 <= n_k-1 <= n_k
        #  -> (n_k-2 + n_k-1) <= 2 * n_k
        # 2. (n_i-1, n_i) <= (n_j-1 + n_j), where i < j
        #  -> if (n_k-2 + n_k-1) <= n_k, then no other adjacent pairs before k-1 is > n_k

        for i in reversed(range(2, n)):
            a, b, c = nums[i], nums[i - 1], nums[i - 2]

            if a >= b + c:
                continue

            return a + b + c

        return 0
