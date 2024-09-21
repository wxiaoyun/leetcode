# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit

from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
      # monotonically increasing deque that contains elements up to the r^th element, in order
      minq = deque() # [small to big between l and r]
      # monotonically decreasing deque that contains elements up to the r^th element, in order
      maxq = deque() # [big to small between l and r]

      # we need this data structure to efficiently shrink the window and know
      # the next biggest/smallest element in the window in O(1)

      longest = 0
      l = 0
      for r in range(len(nums)):
        n = nums[r]

        while maxq and n > maxq[-1]:
          maxq.pop()
        maxq.append(n)

        while minq and n < minq[-1]:
          minq.pop()
        minq.append(n)

        while maxq[0] - minq[0] > limit:
          n = nums[l]
          if n == maxq[0]:
            maxq.popleft()
          if n == minq[0]:
            minq.popleft()
          l += 1
        
        longest = max(longest, r-l+1)
      
      return longest