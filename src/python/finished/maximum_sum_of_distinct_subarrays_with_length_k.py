from collections import deque
from typing import List

# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cur = {}
        q = deque()
        total = 0

        best = 0
        for n in nums:
          q.append(n)
          total += n
          if n not in cur:
            cur[n] = 0
          cur[n] += 1

          if len(q) > k:
            rm = q.popleft()
            total -= rm
            cur[rm] -= 1
            if cur[rm] == 0:
              del cur[rm]
          
          if len(cur) == k:
            best = max(best, total)
        
        return best