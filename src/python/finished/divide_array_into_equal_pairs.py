from typing import List
from collections import Counter

# https://leetcode.com/problems/divide-array-into-equal-pairs


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)

        for _, cnt in c.items():
            if cnt % 2 != 0:
                return False
        return True
