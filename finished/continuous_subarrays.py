from collections import deque
from typing import List

# https://leetcode.com/problems/continuous-subarrays/


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # The front of `inc` tells us what is the minimum element within the sliding window
        # monotonically non-decreasing from left to right
        inc = deque()
        # The front of `dec` tells us what is the maximum element within the sliding window
        # monotonically non-increasing from left to right
        dec = deque()

        total = 0
        l = 0
        for r, n in enumerate(nums):
            # maintain the invariant that the front of `inc` is the smallest element
            while inc and n < nums[inc[-1]]:
                inc.pop()
            inc.append(r)

            # maintain the invariant that the front of `dec` is the largest element
            while dec and n > nums[dec[-1]]:
                dec.pop()
            dec.append(r)

            # shrink the window by increasing the left pointer until the maximal difference
            # within the window is less than or equals to 2
            while inc and dec and (nums[dec[0]] - nums[inc[0]]) > 2:
                if dec[0] == l:
                    dec.popleft()
                if inc[0] == l:
                    inc.popleft()
                l += 1

            total += r - l + 1
        return total


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        inc = deque()  # monotonically non-increasing, so first el is largest
        dec = deque()  # monotonically non-decrease, so first el is smallest

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
