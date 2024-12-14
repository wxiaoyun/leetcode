from collections import deque
from typing import List

# https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        inc = deque() # monotonically non-increasing, so first el is largest
        dec = deque() # monotonically non-decrease, so first el is smallest

        count = 0
        left = 0
        for i, n in enumerate(nums):
          while inc and nums[inc[-1]] < n:
            inc.pop()
          inc.append(i)

          while dec and nums[dec[-1]] > n:
            dec.pop()
          dec.append(i)

          while inc and dec and (nums[inc[0]] - nums[dec[0]]) > 2:
            if inc[0] < dec[0]:
              left = inc.popleft() + 1
            else:
              left = dec.popleft() + 1
          count += i - left + 1
        return count


    # def continuousSubarrays(self, nums: List[int]) -> int:
    #     N = len(nums)

    #     count = 0
    #     for i in range(N):
    #       minn, maxx = nums[i], nums[i]
    #       for j in range(i, N):
    #         minn = min(minn, nums[j])
    #         maxx = max(maxx, nums[j])
    #         if maxx - minn <= 2:
    #           count += 1
    #         else:
    #           break
    #     return count