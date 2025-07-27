from typing import List

# https://leetcode.com/problems/count-hills-and-valleys-in-an-array


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        dedup = []
        for n in nums:
            if dedup and n == dedup[-1]:
                continue
            dedup.append(n)

        count = 0
        for i, n in enumerate(dedup):
            if i == 0 or i == len(dedup) - 1:
                continue

            if (dedup[i - 1] < n and dedup[i + 1] < n) or (
                dedup[i - 1] > n and dedup[i + 1] > n
            ):
                count += 1
        return count
