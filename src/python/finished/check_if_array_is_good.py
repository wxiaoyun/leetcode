from collections import Counter
from typing import List

# https://leetcode.com/problems/check-if-array-is-good


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for i in range(1, len(nums) - 1):
            if cnt[i] != 1:
                return False
        return cnt[len(nums) - 1] == 2
