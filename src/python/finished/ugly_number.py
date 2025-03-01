# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        for fact in [2, 3, 5]:
          while n >= fact and n == n // fact * fact:
            n = n // fact
        return n == 1