from typing import List

# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        # find the maximum strictly increasing subsequence
        inc = [0] * N
        for r in range(N):
          for l in range(r):
            if nums[l] < nums[r]:
              inc[r] = max(inc[r], inc[l] + 1)

        # find the maximum strictly decreasing subsequence
        dec = [0] * N
        for l in reversed(range(N)):
          for r in range(l+1, N):
            if nums[l] > nums[r]:
              dec[l] = max(dec[l], dec[r] + 1)
        
        best = float('inf')
        for i in range(1, N-1):
          if inc[i] > 0 and dec[i] > 0:
            best = min(best, N - inc[i] - dec[i] - 1)
        return best
  
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
          