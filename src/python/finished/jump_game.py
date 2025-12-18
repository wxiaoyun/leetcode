from typing import List

# https://leetcode.com/problems/jump-game/description


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        best = 0
        for i, n in enumerate(nums):
            if i > best:
                return False
            best = max(best, i + n)
        return True
