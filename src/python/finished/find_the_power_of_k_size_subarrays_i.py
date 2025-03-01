from collections import deque
from typing import List

# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # keep track of a monotonic queue that is strictly increasing by 1
        q = deque()
        res = []

        for i, n in enumerate(nums):
          if q and q[0][1] <= i - k:
            q.popleft()

          if not q or n == q[-1][0] + 1:
            q.append((n, i))
          else:
            q.clear()
            q.append((n, i))

          if i >= k - 1:
            if len(q) == k:
              res.append(q[-1][0])
            else:
              res.append(-1)

        return res
        
