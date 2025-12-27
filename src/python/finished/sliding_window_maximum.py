from collections import deque
from typing import List

from sortedcontainers import SortedList


# O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        dq = deque()  # monotonically non-increasing
        for i, ch in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < ch:
                dq.pop()
            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


# O(nlogk)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)

        win = SortedList()
        for i, n in enumerate(nums):
            win.add(n)

            if i >= k:
                prev = nums[i - k]
                win.remove(prev)

            if i >= k - 1:
                res[i - k + 1] = win[-1]

        return res
