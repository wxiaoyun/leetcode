import math
from typing import List

# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # factor(n) = 1 + 2 + ... + n
        #           = n * (n + 1) / 2

        # find minimum t such that, factor(t) * (worktime[0] + ... + worktime[-1]) >= mountain_height

        # Given, w and t, can we calculate h?

        # in `factor(h) * worker_time[w]` seconds, worker w reduces height by h
        # time(w, h) = worker_time[w] * h * (h + 1) / 2
        # t = k * h * (h + 1) / 2
        # 2t/k = h^2 + h
        # 2t/k = (h + 1/2)^2 - (1/2)^2
        # (h + 1/2)^2 = 2t/k + (1/2)^2
        # h = sqrt(2t/k + (1/2)^2) - 1/2

        def height(worker: int, t: int) -> int:
            res = math.floor(
                math.sqrt(2 * t / workerTimes[worker] + (1 / 2) ** 2) - 1 / 2
            )
            # print(f'worker {worker}:{workerTimes[worker]}, t {t}. Reduced {res}')
            return res

        l, r = 0, workerTimes[0] * mountainHeight * (mountainHeight + 1) // 2 + 1
        ans = -1
        while l < r:
            m = l + (r - l) // 2

            total_height = sum(height(w, m) for w in range(len(workerTimes)))

            if total_height < mountainHeight:
                l = m + 1
            else:
                ans = m
                r = m
        return ans
