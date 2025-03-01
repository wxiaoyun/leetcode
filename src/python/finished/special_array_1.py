from typing import List

# https://leetcode.com/problems/special-array-i/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev = nums[0] % 2

        for nxt in nums[1:]:
            parity = nxt % 2
            if prev == parity:
                return False
            prev = parity
        return True