from collections import Counter
from typing import List

# https://leetcode.com/problems/find-the-largest-almost-missing-integer/


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)

        if k == len(nums):
            return max(nums)
        if k == 1:
            return max((k for k, v in cnt.items() if v == 1), default=-1)

        candidates = [nums[0], nums[-1]]
        candidates.sort(reverse=True)
        for c in candidates:
            if cnt[c] == 1:
                return c
        return -1
