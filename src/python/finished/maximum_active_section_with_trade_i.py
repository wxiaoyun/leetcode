# https://leetcode.com/problems/maximize-active-section-with-trade-i


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # ..01..10.. -> ..00..00..

        cur = "1"
        streak = 0
        streaks = []
        for ch in s:
            if ch == cur:
                streak += 1
                continue
            streaks.append(streak)
            streak = 1
            cur = ch
        streaks.append(streak)

        total_ones = sum(streaks[i] for i in range(0, len(streaks), 2))
        best = total_ones
        for i in range(1, len(streaks) - 2, 2):
            best = max(best, total_ones + streaks[i] + streaks[i + 2])
        return best
