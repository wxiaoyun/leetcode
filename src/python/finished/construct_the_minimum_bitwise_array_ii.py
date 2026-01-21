from typing import List

# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ret = [-1] * len(nums)
        for i, n in enumerate(nums):
            ans = -1
            cur = n
            bit = 0
            while cur > 0:
                if cur & 1 == 0:
                    break
                ans = n - (1 << bit)
                bit += 1
                cur >>= 1
            ret[i] = ans
        return ret
