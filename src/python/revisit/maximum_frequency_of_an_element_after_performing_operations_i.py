from collections import Counter, defaultdict
from typing import List


# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)
        deltas = defaultdict(int)
        candidates = set()
        for n in nums:
            deltas[n - k] += 1
            deltas[n + k + 1] -= 1
            candidates.add(n)
            candidates.add(n - k)
            candidates.add(n + k + 1)
        candidates = sorted(list(candidates))

        best = 0
        count = 0
        for cd in candidates:
            count += deltas.get(cd, 0)
            no_ops = cnt.get(cd, 0)
            ops = min(numOperations, count - no_ops)
            best = max(best, no_ops + ops)

        return best
