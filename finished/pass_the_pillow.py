# https://leetcode.com/problems/pass-the-pillow/solutions

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        a = time % (2*(n-1))
        if a < n:
            return a + 1
        else:
            return 2*(n-1) - a + 1
        