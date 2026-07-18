from math import gcd
from typing import List

# https://leetcode.com/problems/find-greatest-common-divisor-of-array/


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn, mx = nums[0], nums[0]
        for n in nums:
            mn, mx = min(mn, n), max(mx, n)
        return gcd(mn, mx)
