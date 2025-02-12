from collections import defaultdict
import heapq
from typing import List

# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        pairs = defaultdict(list)

        def calc_key(n: int) -> int:
            k = 0
            cur = n
            while cur != 0:
                k += cur % 10
                cur = cur // 10
            return k

        for n in nums:
            k = calc_key(n)
            heapq.heappush(pairs[k], n)
            if len(pairs[k]) > 2:
                heapq.heappop(pairs[k])
        
        best = -1
        for l in pairs.values():
            if len(l) < 2:
                continue
            best = max(best, l[0] + l[1])
        return best
