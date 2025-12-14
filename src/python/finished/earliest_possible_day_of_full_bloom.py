from typing import List


# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # We wish to minimise the time of completion

        # Observations:
        # 1. planting must be done serially
        # 2. Growing can be done in parallel

        # Perhaps we should try to "align" the growth such that they
        # finish growing around the same time as closely as possible?
        #

        # Greedy algo:
        # 1. sort plants by growth time
        # 2. Plant the

        n = len(plantTime)
        order = list(range(n))
        order.sort(key=lambda idx: (-growTime[idx]))

        finish_date = 0
        next_free_day = 0
        for idx in order:
            plant_t = plantTime[idx]
            grow_t = growTime[idx]
            next_free_day += plant_t
            finish_date = max(finish_date, next_free_day + grow_t)
        return finish_date
