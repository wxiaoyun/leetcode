from typing import List

# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # to minimise maximum pair value, we need to ensure each pair sum
        # is as similar as possible

        # We can try a greedy approach:
        # pair the largest element with the smallest element

        nums = sorted(nums)
        i, j = 0, len(nums) - 1
        max_pair_sum = 0
        while i < j:
            max_pair_sum = max(max_pair_sum, nums[i] + nums[j])
            i += 1
            j -= 1
        return max_pair_sum
