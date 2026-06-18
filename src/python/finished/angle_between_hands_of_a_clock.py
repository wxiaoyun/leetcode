# https://leetcode.com/problems/angle-between-hands-of-a-clock


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a1 = float(hour % 12 + minutes / 60) / 12.0 * 360
        a2 = float(minutes) / 60.0 * 360

        b = abs(a1 - a2)
        return min(b, 360 - b)
