# https://leetcode.com/problems/find-triangular-sum-of-an-array/


from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        prev = nums
        while len(prev) > 1:
            cur = prev[:-1]
            for i in range(len(prev) - 1):
                cur[i] = (cur[i] + prev[i + 1]) % 10
            prev = cur
        return prev[0]
