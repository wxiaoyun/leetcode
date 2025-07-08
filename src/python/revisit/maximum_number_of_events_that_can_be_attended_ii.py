from typing import List

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        def compute(
            dp: dict, events: List[List[int]], k: int, idx: int, count: int
        ) -> int:
            if count == k or idx >= len(events):
                return 0

            key = (idx, count)
            if key in dp:
                return dp[key]

            best = compute(dp, events, k, idx + 1, count)

            s, e, v = events[idx]
            j = idx + 1
            while j < len(events) and events[j][0] <= e:
                j += 1
            best = max(best, v + compute(dp, events, k, j, count + 1))

            dp[key] = best
            return best

        return compute({}, sorted(events), k, 0, 0)
