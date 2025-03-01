from typing import List

# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
      check = {}
      for n in nums:
        k = abs(n)
        if k not in check:
          check[k] = 0
        
        if n > 0:
          check[k] |= 1
        if n < 0:
          check[k] |= 2
      return max([n if v == 3 else -1 for n, v in check.items()])