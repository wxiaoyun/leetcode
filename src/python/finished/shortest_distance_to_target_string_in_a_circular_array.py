from typing import List

# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        INF = 1 << 32
        ans = INF
        for i, w in enumerate(words):
            if w != target:
                continue

            ans = min(
                ans,
                abs(i - startIndex),
                abs(i + len(words) - startIndex),
                abs(i - len(words) - startIndex),
            )
        return ans if ans < INF else -1
