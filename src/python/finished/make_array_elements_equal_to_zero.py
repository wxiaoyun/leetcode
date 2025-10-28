from typing import List

# https://leetcode.com/problems/make-array-elements-equal-to-zero/


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # observation: a position i is valid if
        # (1): nums[i] == 0
        # (2):
        #    either: left sum == right sum
        #    or    : left sum + (1 if initial dir left else 0) == right sum + (1 if initial dir right else 0)

        # psum[i] == sum(nums[:i]) exclusive of i
        psum = [0]
        for n in nums:
            psum.append(psum[-1] + n)

        valid_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                continue

            left_sum = psum[i]
            right_sum = psum[-1] - left_sum

            if left_sum == right_sum:
                valid_pos += 2
            elif abs(left_sum - right_sum) <= 1:
                valid_pos += 1

        return valid_pos
