# https://leetcode.com/problems/count-good-numbers/


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        evens = 10 // 2
        primes = len([2, 3, 5, 7])

        n_half = n // 2

        res = 1
        res = res * pow(evens, n_half, MOD)
        res = res * pow(primes, n_half, MOD)
        if n % 2 == 1:
            res = res * evens

        res = res % MOD
        return res
