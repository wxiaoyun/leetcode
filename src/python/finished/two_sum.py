from typing import List

# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            # target = n + need
            need = target - n

            for j in seen.setdefault(need, []):
                return (i, j)

            seen.setdefault(n, []).append(i)

        return []