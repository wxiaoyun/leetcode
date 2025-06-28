from typing import List
import heapq

# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for i, n in enumerate(nums):
            heapq.heappush(pq, (n, i))
            if len(pq) > k:
                heapq.heappop(pq)

        pq.sort(key=lambda x: x[1])
        return [n for n, i in pq]
