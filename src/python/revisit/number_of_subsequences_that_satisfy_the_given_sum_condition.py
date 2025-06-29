from typing import List

# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        nums.sort()

        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % MOD

        left, right = 0, n - 1
        result = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                num_elements_in_between = right - left
                result = (result + powers[num_elements_in_between]) % MOD

                left += 1
            else:
                right -= 1

        return result
