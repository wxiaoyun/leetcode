import heapq
from typing import List

# https://leetcode.com/problems/maximum-average-pass-ratio/


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        cls_nf = []
        full_count = 0
        for p, t in classes:
            if p < t:
                cls_nf.append(((p - t) / (t**2 + t), p, t))
            else:
                full_count += 1

        if len(cls_nf) == 0:
            return 1

        heapq.heapify(cls_nf)
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(cls_nf)
            p, t = p + 1, t + 1
            heapq.heappush(cls_nf, ((p - t) / (t**2 + t), p, t))
        return (sum([p / t for _, p, t in cls_nf]) + full_count) / (
            len(cls_nf) + full_count
        )
