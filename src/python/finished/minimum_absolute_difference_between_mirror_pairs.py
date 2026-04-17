from typing import List

# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(n: int) -> int:
            nstr = str(n)
            nrev = 0
            for d in reversed(nstr):
                nrev = (nrev * 10) + int(d)
            return nrev

        INF = 1 << 32

        lookup = {}
        best = INF
        for i, n in enumerate(nums):
            if n in lookup:
                best = min(best, i - lookup[n])
            lookup[rev(n)] = i

        return best if best < INF else -1
