from typing import List

# https://leetcode.com/problems/keep-multiplying-found-values-by-two/


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        seen = set(nums)
        target = original
        while target in seen:
            target <<= 1
        return target
