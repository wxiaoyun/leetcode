import heapq
from typing import List

# https://leetcode.com/problems/maximum-average-pass-ratio/
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # (a + 1) / (a + b + 1)

        # 1/2 = 0.5 | 2/3 = 0.66 | inc = 0.16
        # 2/3 = 0.66 | 3/4 = 0.75 | inc = 0.0833333333
        # the larger the base, the smaller the inc

        # Increase is given by
        # (a + 1) / (a + b + 1) - a/(a+b)
        # = ((a+1)(a+b) - a(a+b+1)) / ((a+b)*(a+b+1))

        def compute_inc(pas: int, total: int, inc: int = 1) -> float:
            return ((pas + inc) * (total) - pas * (total + inc)) / (
                (total) * (total + inc)
            )

        pq = [(-compute_inc(pas, total), pas, total) for pas, total in classes]
        heapq.heapify(pq)

        for _ in range(extraStudents):
            _, pas, total = heapq.heappop(pq)
            new_pas = pas + 1
            new_total = total + 1
            heapq.heappush(pq, (-compute_inc(new_pas, new_total), new_pas, new_total))

        ratio_sum = sum(pas / total for _, pas, total in pq)
        ratio_avg = ratio_sum / len(pq)
        return ratio_avg


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
