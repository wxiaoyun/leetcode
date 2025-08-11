# https://leetcode.com/problems/range-product-queries-of-powers


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        p = 0
        while n > 0:
            comp = (n & 1) << p
            if comp:
                powers.append(comp)
            p += 1
            n >>= 1
        pprod = [1]  # pprod[i] = powers[0] * ... * powers[i - 1]
        for p in powers:
            pprod.append(p * pprod[-1])

        MOD = int(1e9 + 7)
        Q = len(queries)
        ret = [0] * Q
        for i, (l, r) in enumerate(queries):
            ret[i] = (pprod[r + 1] // pprod[l]) % MOD
        return ret
