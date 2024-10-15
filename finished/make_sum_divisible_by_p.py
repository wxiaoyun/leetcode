from typing import List

# https://leetcode.com/problems/make-sum-divisible-by-p/

# Intuition
# Essentially, we are trying to find i, j such that:
# (total - prefix_sum[j] + prefix_sum[i]) % p = 0
# total - prefix_sum[j] + prefix_sum[i] = kp, where k is a positive integer
# prefix_sum[i] = kp - total + prefix_sum[j]
# prefix_sum[i] % p  = (kp - total + prefix_sum[j]) % p
# prefix_sum[i] % p  = (kp) % p + (-total + prefix_sum[j]) % p
# prefix_sum[i] % p  = (prefix_sum[j] - total) % p
# modulo_prefix_sum[i] = (prefix_sum[j] - total) % p

# With this equation, we can iterate through the array and store the most recent index
# of a modulo prefix sum. (Most recent since we want the smallest subarray removed)
# Then we take the minimum as we iterate

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        prefix_sum = [nums[0]%p]

        for n in nums[1:]:
          prefix_sum.append((prefix_sum[-1]+n)%p)
        
        if prefix_sum[-1] == 0:
          return 0

        last_seen = {
          0: -1
        }

        best = float('inf')
        for i in range(N):
          target = (prefix_sum[i] - prefix_sum[-1]) % p
          if target in last_seen:
            comp_idx = last_seen[target]
            best = min(best, i-comp_idx)
          last_seen[prefix_sum[i]] = i

        if best == N:
          return -1

        return best