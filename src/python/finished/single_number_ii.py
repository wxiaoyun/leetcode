# https://leetcode.com/problems/single-number-ii/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for i in range(32):
            tmp = 0
            for n in nums:
                n &= (1<<32)-1
                tmp += (n>>i)&1
            tmp %= 3
            res |= tmp << i

        if res >= 1<<31:
            res -= 1<<32
        
        return res