# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

import heapq
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        nnn = len(nums)
        N = nnn // 3

        pq1 = [-n for n in nums[:N]]
        heapq.heapify(pq1)
        arr1 = [sum(nums[:N])]
        for n in nums[N : 2 * N]:
            sm = arr1[-1] + n
            heapq.heappush(pq1, -n)
            sm += heapq.heappop(pq1)
            arr1.append(sm)

        pq2 = list(nums[2 * N :])
        heapq.heapify(pq2)
        arr2 = [sum(nums[2 * N :])]
        for n in reversed(nums[N : 2 * N]):
            sm = arr2[-1] + n
            heapq.heappush(pq2, n)
            sm -= heapq.heappop(pq2)
            arr2.append(sm)

        return min((arr1[i] - arr2[N - i]) for i in range(N + 1))
