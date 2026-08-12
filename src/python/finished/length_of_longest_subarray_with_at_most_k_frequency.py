import heapq
from collections import deque
from typing import List

# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        occurence = {}

        best = 0
        left = 0

        pq = []
        deleted = set()

        for i in range(len(nums)):
            n = nums[i]
            dq = occurence.setdefault(n, deque())
            dq.append(i)
            heapq.heappush(pq, i)

            if len(dq) > k:
                l = dq.popleft()
                left = max(left, l + 1)
                deleted.add(l)

            while pq and pq[0] in deleted:
                d = heapq.heappop(pq)
                deleted.remove(d)

            # print(i)
            # print(left)
            # print(pq)
            # print()

            l = 0 if not pq else pq[0]
            l = max(left, l)
            best = max(best, i - l + 1)

        return best
