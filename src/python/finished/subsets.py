# https://leetcode.com/problems/subsets/

import copy
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(accum: List[List[int]], i: int) -> List[List[int]]:
            if i >= len(nums):
                return accum
            
            cp = copy.deepcopy(accum)

            for r in cp:
                r.append(nums[i])
            
            cp.extend(accum)
            return helper(cp, i+1)
        
        return helper([[]], 0)
        
