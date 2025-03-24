from typing import List

# https://leetcode.com/problems/count-days-without-meetings


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)

        # merge meetings
        merged_m = []
        prev_s, prev_e = None, None
        for s, e in meetings:
            if not prev_s:
                prev_s, prev_e = s, e
                continue

            if s <= prev_e:
                prev_e = max(prev_e, e)
                continue

            merged_m.append((prev_s, prev_e))
            prev_s, prev_e = s, e

        if prev_s:
            merged_m.append((prev_s, prev_e))

        free_days = 0
        t = 0
        for s, e in merged_m:

            free_days += s - t - 1
            t = e

        free_days += days - t
        return free_days
