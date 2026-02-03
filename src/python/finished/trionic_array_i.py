from typing import List

# https://leetcode.com/problems/trionic-array-i


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) <= 3:
            return False

        direction = 1
        n_flip = 0
        streak = 0

        for i in range(1, len(nums)):
            prev, cur = nums[i - 1], nums[i]
            if prev == cur:
                return False

            should_flip = False
            if direction > 0:
                should_flip = not prev < cur
            else:
                should_flip = not prev > cur

            if should_flip:
                if streak < 1:
                    return False
                n_flip += 1
                direction *= -1
                streak += 1
            else:
                streak = 1

        return n_flip == 2
