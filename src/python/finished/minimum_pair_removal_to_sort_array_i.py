from typing import List

# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        nums = nums[:]

        def is_sorted(nums: List[int]) -> bool:
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
            return True

        removals = 0
        while not is_sorted(nums):
            pair_sum = 1 << 31
            pair_idx = -1

            for i in range(1, len(nums)):
                local_pair_sum = nums[i - 1] + nums[i]
                if local_pair_sum < pair_sum:
                    pair_sum = local_pair_sum
                    pair_idx = i

            nums.pop(pair_idx)
            nums.pop(pair_idx - 1)
            nums.insert(pair_idx - 1, pair_sum)
            removals += 1

        return removals
