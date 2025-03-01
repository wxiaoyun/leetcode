# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays

from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tcnt = Counter(target)
        acnt = Counter(arr)
        return tcnt == acnt