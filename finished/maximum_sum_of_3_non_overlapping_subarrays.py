from typing import List

# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        dp1 = {}
        dp2 = {}
        dp3 = {}

        prefix_sum = [0]
        for i in range(N):
          prefix_sum.append(nums[i] + prefix_sum[-1])
        
        # array sum from i to j exclusive: [i, j)
        def subarr_sum(i, j):
          return prefix_sum[j] - prefix_sum[i]

        for i in reversed(range(N-k+1)):
          s = subarr_sum(i, i + k)
          ls = [i]
          if i+1 in dp1:
            ps, pls = dp1[i+1]
            if ps > s:
              s = ps
              ls = pls

          dp1[i] = (s, ls)

        for i in reversed(range(N-k+1)):
          prev = i + k
          if prev not in dp1:
            continue

          ps, pls = dp1[i + k]
          s = ps
          s += subarr_sum(i, i + k)
          ls = pls[:]
          ls.append(i)

          if i+1 in dp2:
            ps, pls = dp2[i+1]
            if ps > s:
              s = ps
              ls = pls
          
          dp2[i] = (s, ls)
        
        for i in reversed(range(N-k+1)):
          prev = i + k
          if prev not in dp2:
            continue

          ps, pls = dp2[i + k]
          s = ps
          s += subarr_sum(i, i + k)
          ls = pls[:]
          ls.append(i)

          if i+1 in dp3:
            ps, pls = dp3[i+1]
            if ps > s:
              s = ps
              ls = pls
          
          dp3[i] = (s, ls)
        
        res = dp3[0][1]
        res.reverse()
        return res
