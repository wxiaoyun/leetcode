from typing import List

# https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) + 1):
            ans ^= i ^ (nums[i] if i < len(nums) else 0)
        return ans
