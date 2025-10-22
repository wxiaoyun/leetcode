from collections import defaultdict
from typing import List


# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        deltas = defaultdict(int)
        candidates = set()
        for n in nums:
            cnt[n] += 1
            deltas[n - k] += 1
            deltas[n + k + 1] -= 1
            candidates.add(n)
            candidates.add(n - k)
            candidates.add(n + k + 1)

        total, best = 0, 0
        for n in sorted(list(candidates)):
            total += deltas[n]
            n_cnt = cnt[n]
            ops = min(numOperations, total - n_cnt)
            best = max(best, ops + n_cnt)
        return best
