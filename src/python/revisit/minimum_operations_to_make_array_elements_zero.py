# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

import math
from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # n:   1, 4, 16, 64, 256, 1024
        # ops: 0, 1,  2,  3,   4,   5,    6
        n = [1]
        cur = 4
        while cur <= 1e9:
            n.append(cur)
            cur = cur << 2

        def count_ops(num: int) -> int:
            log4 = math.ceil(math.log(num, 4)) if num > 1 else 1
            opcount = 0
            for i in range(1, log4):
                opcount += i * (n[i] - n[i - 1])
            opcount += log4 * (num - n[log4 - 1])
            return opcount

        return sum(math.ceil((count_ops(r + 1) - count_ops(l)) / 2) for l, r in queries)
