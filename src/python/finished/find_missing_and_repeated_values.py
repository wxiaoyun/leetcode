from typing import List

# https://leetcode.com/problems/find-missing-and-repeated-values


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        nums = set([i + 1 for i in range(N**2)])

        res = [-1, -1]
        for row in grid:
            for n in row:
                if n in nums:
                    nums.remove(n)
                else:
                    res[0] = n

        for n in nums:
            res[1] = n

        return res
