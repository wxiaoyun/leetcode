# https://leetcode.com/problems/power-of-three


import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        x = math.log(n, 3)
        return abs(x - round(x)) < 1e-10
