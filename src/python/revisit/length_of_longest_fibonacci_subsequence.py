from collections import defaultdict
from typing import List

# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        N = len(arr)
        lookup = {n: i for i, n in enumerate(arr)}

        dp = defaultdict(int)
        best = 0
        for k, kval in enumerate(arr):
            for j, jval in enumerate(arr[:k]):
                ival = kval - jval
                if ival >= jval:
                    continue

                pair = (j, k)
                if ival not in lookup:
                    dp[pair] = max(dp[pair], 2)
                    continue

                i = lookup[ival]
                prev_pair = (i, j)
                dp[pair] = max(dp[pair], (dp[prev_pair] or 2) + 1)
                best = max(best, dp[pair])

        return best

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        N = len(arr)
        lookup = {n: i for i, n in enumerate(arr)}

        def best(i: int, fib: list) -> int:
            if i >= N:
                return len(fib)

            res = len(fib)

            if len(fib) < 2:
                res = max(res, best(i + 1, fib))

            fib.append(arr[i])
            res = max(res, len(fib))

            if len(fib) < 2:
                res = max(res, best(i + 1, fib))
            else:
                nxt = fib[-1] + fib[-2]
                if nxt in lookup:
                    res = max(res, best(lookup[nxt], fib))

            fib.pop()
            return res

        res = best(0, [])
        return res if res >= 3 else 0
