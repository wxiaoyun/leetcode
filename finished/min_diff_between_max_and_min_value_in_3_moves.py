# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves

from copy import copy
import heapq
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # if len(nums) <= 4:
        #     return 0

        # nums.sort()
        # first4 = nums[0:4]
        # last4 = nums[-4:]
        
        # best = float('inf')
        # for i in range(4):
        #     heuristic = last4[-4+i] - first4[i]            
        #     best = min(best, heuristic)

        # return best

        if len(nums) <= 4:
            return 0
        
        dup = copy.deepcopy(nums)
        first4 = heapq.nsmallest(4, nums)
        last4 = heapq.nlargest(4, dup)

        best = float('inf')
        for i in range(4):
            diff = last4[-i-1] - first4[i]
            best = min(best, abs(diff))
        return best
