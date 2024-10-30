from typing import List

# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        ltr_lis = [1] * n
        rtl_lis = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    ltr_lis[i] = max(ltr_lis[i], ltr_lis[j] + 1)
        for i in reversed(range(n)):
            for j in reversed(range(i, n)):
                if nums[i] > nums[j]:
                    rtl_lis[i] = max(rtl_lis[i], rtl_lis[j] + 1)
    
        best = 0
        for i in range(1, n-1):
          if ltr_lis[i] > 1 and rtl_lis[i] > 1:
            best = max(best, ltr_lis[i]+rtl_lis[i]-1)
        return n-best
          