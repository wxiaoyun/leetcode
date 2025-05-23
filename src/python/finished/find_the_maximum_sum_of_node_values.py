from typing import List

# https://leetcode.com/problems/find-the-maximum-sum-of-node-values


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        tmp = [(n ^ k) - n for n in nums]
        tmp.sort(reverse=True)

        total = sum(nums)
        for i in range(0, len(nums) - 1, 2):
            total = max(total, total + tmp[i] + tmp[i + 1])

        return total
