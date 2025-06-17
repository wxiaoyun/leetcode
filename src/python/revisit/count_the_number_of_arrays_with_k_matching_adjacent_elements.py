# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        res = math.comb(n - 1, k) % MOD
        res = (res * m) % MOD
        res = (res * pow(m - 1, n - k - 1, MOD)) % MOD
        return res
