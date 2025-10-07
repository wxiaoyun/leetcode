from typing import List
from sortedcontainers import SortedList

# https://leetcode.com/problems/avoid-flood-in-the-city/


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n

        # Dict<lake, day_of_rain>
        full_lake = {}
        drains = SortedList()
        for day, lake in enumerate(rains):
            if lake == 0:
                drains.add(day)
                continue

            if lake not in full_lake:
                full_lake[lake] = day
                continue

            day_of_rain = full_lake[lake]
            full_lake[lake] = day
            idx = drains.bisect_right(day_of_rain)
            if idx >= len(drains):
                return []

            drain_day = drains[idx]
            drains.pop(idx)
            ans[drain_day] = lake

        for day in drains:
            ans[day] = 1

        return ans
