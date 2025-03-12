from typing import List

# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N

        while l < r:
            m = l + (r - l) // 2
            val = nums[m]

            if val < 0:
                l = m + 1
            else:
                r = m
        

        if l < N and nums[l] == 0:
            l_low = l

            l, r = 0, N

            while l < r:
                m = l + (r - l) // 2
                val = nums[m]

                if val <= 0:
                    l = m + 1
                else:
                    r = m

            return max(l_low, N - (l + 1 - 1))
        
        return max(l, N - l)
            
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        for n in nums:
            if n > 0:
                pos += 1
            elif n < 0:
                neg += 1
        return max(pos, neg)