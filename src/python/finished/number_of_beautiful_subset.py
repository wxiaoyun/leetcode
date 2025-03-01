# https://leetcode.com/problems/the-number-of-beautiful-subsets

from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        
        def helper(i):
            if i >= len(nums):
                return 1
            
            res = helper(i+1)

            if freq[nums[i]+k] == 0 and freq[nums[i]-k] == 0:
                freq[nums[i]]+=1
                res += helper(i+1)
                freq[nums[i]]-=1
            
            return res
        
        return helper(0)-1
