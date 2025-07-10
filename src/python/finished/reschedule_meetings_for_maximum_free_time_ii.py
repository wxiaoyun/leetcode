from typing import List
import heapq

# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        # <slack><event><slack> -> move <event> to another slot
        # Question: is there another slack that is big enough for the event?

        n = len(startTime)
        slacks = [0] * (n + 1)
        top_slacks = []
        prev_end = 0
        for i in range(n + 1):
            s, e = (startTime[i], endTime[i]) if i < n else (eventTime, 0)

            slack = s - prev_end
            slacks[i] = slack

            heapq.heappush(top_slacks, (slack, i))
            if len(top_slacks) > 3:
                heapq.heappop(top_slacks)
            prev_end = e

        best = 0
        for i in range(n):
            s, e = startTime[i], endTime[i]
            slack_sum = sum(slacks[i : i + 2])
            best = max(best, slack_sum)

            duration = e - s
            for slack, j in top_slacks:
                if slack >= duration and j != i and j != i + 1:
                    best = max(best, slack_sum + duration)

        return best
