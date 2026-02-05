from typing import List

# https://leetcode.com/problems/transformed-array/


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        for i, a in enumerate(nums):
            if a >= 0:
                result[i] = nums[(i + a) % n]
            else:
                result[i] = nums[(i - abs(a)) % n]

        return result
