# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_neg = n < 0
        if is_neg:
            n = -n

        accum = 1
        while n != 0:
            if n % 2 == 1:
                accum *= x
                n -= 1
            else:
                x = x * x
                n //= 2

        if is_neg:
            accum = 1 / accum
        return accum


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x: float, n: int, accum: int = 1) -> float:
            if n == 0:
                return accum

            if n < 0:
                return 1 / helper(x, -n, accum)

            if n % 2 == 1:
                return helper(x, n - 1, accum * x)

            return helper(x * x, n // 2, accum)

        return helper(x, n)
