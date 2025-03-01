# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

# Time: O(n*max)
# Space: O(n*max)
from typing import Dict, List, Tuple


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = 0
        for n in nums:
          maximum |= n
        
        dp: Dict[Tuple[int, int], int] = {} # Dict[(idx, or_val), int]
        def helper(target: int, accum: int, i: int) -> int:
          key = (i, accum)
          if key in dp:
            return dp[key]

          res = 0
            # Continue to find other combinations
          if i >= len(nums):
            if accum == target:
              res += 1
            return res
          
          # Take
          res += helper(maximum, accum | nums[i], i+1)
          # No take
          res += helper(maximum, accum, i+1)
          dp[key] = res
          return res
        
        return helper(maximum, 0, 0)

# Time: O(2^n)
# Space: O(1)
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = 0
        for n in nums:
          maximum |= n
        
        def helper(target: int, accum: int, i: int) -> int:
          res = 0
            # Continue to find other combinations
          if i >= len(nums):
            if accum == target:
              res += 1
            return res
          
          # Take
          res += helper(maximum, accum | nums[i], i+1)
          # No take
          res += helper(maximum, accum, i+1)
          return res
        
        return helper(maximum, 0, 0)