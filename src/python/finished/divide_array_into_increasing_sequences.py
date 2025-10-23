from typing import List

# https://leetcode.com/problems/divide-array-into-increasing-sequences/


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        num, ncnt = -1, 0
        for n in nums:
            if n == num:
                ncnt += 1
            else:
                num = n
                ncnt = 1

            if k * ncnt > len(nums):
                return False

        return True
