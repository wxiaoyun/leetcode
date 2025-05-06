from typing import List

# https://leetcode.com/problems/build-array-from-permutation


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        for i in range(N):
            ans[i] = nums[nums[i]]
        return ans
