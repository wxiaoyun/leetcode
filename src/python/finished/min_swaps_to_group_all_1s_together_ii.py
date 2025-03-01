# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii


from collections import Counter
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count = Counter(nums)
        ones = count[1]

        n = len(nums)
        i = 0
        zeros = 0
        min_swap = float('inf')
        for j in range(n*2):
            while j-i+1 > ones:
                if nums[i%n] == 0:
                    zeros -= 1
                i += 1
            
            if nums[j%n] == 0:
                zeros += 1
            
            if j-i+1 < ones:
                continue
            
            min_swap = min(min_swap, zeros)

        return min_swap