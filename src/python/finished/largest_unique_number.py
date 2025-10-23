from collections import Counter
from typing import List

# https://leetcode.com/problems/largest-unique-number/


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        num = -1
        for n, f in cnt.items():
            if f != 1:
                continue
            num = max(num, n)
        return num
