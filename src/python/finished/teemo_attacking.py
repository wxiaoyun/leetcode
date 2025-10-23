from typing import List, Optional, Tuple

# https://leetcode.com/problems/teemo-attacking/


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0 or duration <= 0:
            return 0

        total_duration_under_poison = 0
        for i in range(1, len(timeSeries)):
            prev_interval_start = timeSeries[i - 1]
            prev_interval_end = prev_interval_start + duration  # exclusive
            cur_interval_start = timeSeries[i]

            if prev_interval_end <= cur_interval_start:
                total_duration_under_poison += duration
                continue

            # overlap exists
            # calculate overlap

            # s1          e1
            #       s2            e2

            # (1, 3), (2, 4)
            overlap = prev_interval_end - cur_interval_start
            total_duration_under_poison += duration - overlap

        # add the poison duration of the last attack
        total_duration_under_poison += duration
        return total_duration_under_poison


class PoisonedIntervalIterator:
    def __init__(self, timeSeries: List[int], duration: int):
        self.t_index = 0
        self.is_valid = len(timeSeries) > 0 and duration > 0
        self.timeSeries = timeSeries
        self.duration = duration
        return None

    def next(self) -> Optional[Tuple[int, int]]:
        timeSeries = self.timeSeries
        if not self.is_valid or self.t_index >= len(timeSeries):
            return None

        duration = self.duration
        interval_start = timeSeries[self.t_index]
        interval_end = interval_start + duration
        self.t_index += 1

        while self.t_index < len(timeSeries):
            next_interval_start = timeSeries[self.t_index]

            if next_interval_start < interval_end:
                # if theres overlap, merge and continue
                interval_end = next_interval_start + duration
                self.t_index += 1
                continue

            # if there is no overlap, return the current interval
            return (interval_start, interval_end)

        return (interval_start, interval_end)
