from typing import List

# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique = set(nums)

        greater = 0
        _min = float("inf")
        for v in unique:
            if v > k:
                greater += 1
            _min = min(_min, v)

        if k > _min:
            return -1

        return greater
