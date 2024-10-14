from typing import List

# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N # dp[i] = longest increasing sequence that ends with nums[i]

        best = 1
        for idx_r, r in enumerate(nums):
          for idx_l, l in enumerate(nums[:idx_r]):
            if l >= r:
              continue
            dp[idx_r] = max(dp[idx_r], dp[idx_l]+1)
            best = max(best, dp[idx_r])
        return best