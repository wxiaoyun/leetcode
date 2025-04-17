from collections import defaultdict
from typing import List

# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        seen = defaultdict(list)
        total = 0
        for i, n in enumerate(nums):
            for j in seen[n]:
                if (i * j) % k == 0:
                    total += 1
            seen[n].append(i)
        return total
