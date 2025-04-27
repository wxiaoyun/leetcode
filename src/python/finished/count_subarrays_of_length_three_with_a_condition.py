from typing import List

# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0

        for i in range(2, len(nums)):
            a, b, c = nums[i - 2], nums[i - 1], nums[i]
            if b == (a + c) * 2:
                count += 1

        return count
