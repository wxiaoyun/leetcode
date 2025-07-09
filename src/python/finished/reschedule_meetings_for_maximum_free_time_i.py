from typing import List

# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        # move 1 block -> merge 2 adjacent slack
        # x    x.     x.      x.     x
        # x    x.                  xxx
        # move 2 block -> merge 3 adjacent slack

        n = len(startTime)
        prev_end = 0
        slacks = []
        for i in range(n):
            s, e = startTime[i], endTime[i]
            slacks.append(s - prev_end)
            prev_end = e
        slacks.append(eventTime - prev_end)

        best = sum(slacks[: k + 1])
        cur = best
        for i in range(k + 1, len(slacks)):
            cur = cur + slacks[i] - slacks[i - k - 1]
            best = max(best, cur)
        return best
