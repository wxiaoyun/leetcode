from typing import List

# https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        diffs = set([0]) 
        for n in nums:
            new_diffs = set()
            for d in diffs:
                new_diffs.add(abs(n - d)) 
                new_diffs.add(n + d) 
            diffs = new_diffs
            
        return 0 in diffs

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