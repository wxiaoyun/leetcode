# https://leetcode.com/problems/power-of-four/


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            tmp = n // 4 * 4
            if tmp != n:
                return False
            n = n // 4
        return True
