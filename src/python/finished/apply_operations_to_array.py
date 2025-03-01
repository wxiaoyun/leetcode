from typing import List

# https://leetcode.com/problems/apply-operations-to-an-array


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        j = 0

        for i in range(N):
            if i + 1 < N and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums
