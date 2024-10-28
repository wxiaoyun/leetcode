from typing import List

# https://leetcode.com/problems/longest-square-streak-in-an-array/

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        squares = set(nums)
        best = 0
        for n in nums:
          cur = n ** 2
          length = 1
          while cur in squares:
            cur = cur ** 2
            length += 1
            best = max(best, length)
        
        return best if best > 1 else -1
