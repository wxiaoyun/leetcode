import math


# https://leetcode.com/problems/count-square-sum-triples/


class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            for j in range(1, i):
                asq = i ** 2
                bsq = j ** 2
                csq = asq + bsq
                c = math.floor(math.sqrt(csq))
                if c <= n and c ** 2 == csq:
                    cnt += 2
        return cnt
