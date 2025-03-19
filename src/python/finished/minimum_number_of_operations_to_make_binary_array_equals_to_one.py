from typing import List

# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        flips = 0
        for i in range(N - 2):
            if nums[i] != 0:
                continue

            for j in range(i, i + 3):
                nums[j] ^= 1

            flips += 1

        for i in range(N - 2, N):
            if nums[i] == 0:
                return -1

        return flips
