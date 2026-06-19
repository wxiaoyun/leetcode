from typing import List

# https://leetcode.com/problems/find-the-highest-altitude


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest, cur = 0, 0
        for delta in gain:
            cur += delta
            highest = max(highest, cur)
        return highest
