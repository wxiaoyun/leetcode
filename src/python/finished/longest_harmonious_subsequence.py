from typing import List
from collections import defaultdict

# https://leetcode.com/problems/longest-harmonious-subsequence


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        lens = defaultdict(int)
        check = defaultdict(int)
        for n in nums:
            lens[n] += 1
            check[n] |= 0b01
            lens[n - 1] += 1
            check[n - 1] |= 0b10
        filtered = list(v for n, v in lens.items() if check.get(n) == 0b11)
        return 0 if not filtered else max(filtered)
