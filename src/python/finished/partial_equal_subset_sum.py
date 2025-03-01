from typing import List

# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = {}
        def check(s: int, i: int) -> bool:
            if i >= len(nums):
                return s == 0
            
            key = (s, i)
            if key in dp:
                return dp[key]
            
            num = nums[i]
            res = check(s-num, i+1) or check(s, i+1)
            dp[key] = res
            return res
        
        return check(target, 0)