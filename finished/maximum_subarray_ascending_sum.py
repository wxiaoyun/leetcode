from typing import List

# https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        N = len(nums)
        best = -1

        i = 0
        while i < N:
            cur = 0
            
            prev = -float("inf")
            while i < N:
                n = nums[i]
                if prev < n:
                    cur += n
                    i += 1
                    prev = n
                else:
                    break
            
            best = max(best, cur)
        
        return best