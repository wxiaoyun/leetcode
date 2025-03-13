from typing import List

# https://leetcode.com/problems/zero-array-transformation-ii


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)

        delta = [0] * (N + 1)
        q = 0
        for i, n in enumerate(nums):
            while delta[i] < n:
                if q >= len(queries):
                    return -1

                l, r, v = queries[q]
                q += 1
                if r < i:
                    continue

                delta[max(i, l)] += v
                delta[r + 1] -= v

            delta[i + 1] += delta[i]

        return q
