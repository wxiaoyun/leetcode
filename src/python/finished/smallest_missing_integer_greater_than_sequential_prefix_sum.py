from typing import List

# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq_streak = nums[0]
        present = [False] * 52
        present[nums[0]] = True
        prefix_break = False
        for i in range(1, len(nums)):
            present[nums[i]] = True

            if nums[i] != nums[i - 1] + 1:
                prefix_break = True
            if prefix_break:
                continue

            seq_streak += nums[i]

        for x in range(seq_streak, 52):
            if not present[x]:
                return x
        return seq_streak
