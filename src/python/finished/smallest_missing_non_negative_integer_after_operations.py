from typing import List

# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        classes = [0] * value

        for n in nums:
            clas = n % value
            classes[clas] += 1

        min_cnt = min(classes)
        for k, cnt in enumerate(classes):
            if cnt == min_cnt:
                return cnt * value + k
        return -1
