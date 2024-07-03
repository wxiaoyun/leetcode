# https://leetcode.com/problems/count-number-of-nice-subarrays

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res, odd_cnt = 0, 0
        l, m = 0, 0

        for r in range(len(nums)):
            if (nums[r]%2) == 1:
                odd_cnt += 1
            
            while odd_cnt > k:
                if (nums[l]%2) == 1:
                    odd_cnt -= 1
                l += 1
            
            if odd_cnt == k:
                m = l
                while (nums[m]%2) == 0:
                    m += 1
                
                res += m-l+1
        
        return res