# https://leetcode.com/problems/maximum-number-of-balloons/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = {ch: 0 for ch in "balloon"}
        for ch in text:
            if ch in cnt:
                cnt[ch] += 1

        n_instance = {ch: cnt[ch] // "balloon".count(ch) for ch in "balloon"}
        return min(n_instance.values())
