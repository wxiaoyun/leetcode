import heapq
from typing import List

# https://leetcode.com/problems/minimum-index-of-a-valid-split


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        cnt = {}
        pq = []

        predom = [-1] * N
        for i, n in enumerate(nums):
            new_cnt = cnt.get(n, 0) + 1
            cnt[n] = new_cnt

            heapq.heappush(pq, (new_cnt, n))
            if len(pq) > 1:
                heapq.heappop(pq)

            f, v = pq[0]
            if f > (i + 1) // 2:
                predom[i] = v

        cnt.clear()
        pq.clear()

        posdom = [-2] * N
        for i in reversed(range(N)):
            n = nums[i]
            new_cnt = cnt.get(n, 0) + 1
            cnt[n] = new_cnt

            heapq.heappush(pq, (new_cnt, n))
            if len(pq) > 1:
                heapq.heappop(pq)

            f, v = pq[0]
            if f > (N - i) // 2:
                posdom[i] = v

        for i in range(N - 1):
            if predom[i] == posdom[i + 1]:
                return i
        return -1
