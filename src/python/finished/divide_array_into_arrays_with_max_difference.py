from typing import List

# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        groups = []

        for n in nums:
            if not groups or len(groups[-1]) == 3:
                groups.append([n])
                continue
            if n > groups[-1][0] + k:
                return []

            groups[-1].append(n)

        return groups
