from typing import List

# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dup = []
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                dup.append(n)
        return dup
