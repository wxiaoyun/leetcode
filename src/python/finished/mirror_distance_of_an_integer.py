# https://leetcode.com/problems/mirror-distance-of-an-integer/


class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_mirror = 0
        tmp = n
        while tmp != 0:
            n_mirror = (n_mirror * 10) + tmp % 10
            tmp //= 10
        return abs(n_mirror - n)
