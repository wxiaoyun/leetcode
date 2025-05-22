import heapq
from typing import List

# https://leetcode.com/problems/zero-array-transformation-iii


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        Q = len(queries)
        prefix_delta = [0] * (N + 1)

        queries.sort()
        q = 0
        pq = []
        cur_delta = 0

        for i, n in enumerate(nums):
            cur_delta += prefix_delta[i]

            while q < Q and queries[q][0] == i:
                s, e = queries[q]
                heapq.heappush(pq, (-e, s, e))
                q += 1

            while n > cur_delta:
                if not pq:
                    return -1

                _, s, e = heapq.heappop(pq)
                if e < i:  # cannot form 0
                    return -1

                cur_delta += 1
                prefix_delta[e + 1] -= 1

        return len(pq)
