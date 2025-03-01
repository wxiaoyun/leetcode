# https://leetcode.com/problems/sort-colors

from collections import Counter
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # cnt = Counter(nums)

        # cur = 0
        # for i in range(cnt[0]):
        #     nums[cur+i] = 0
        # cur += cnt[0]
        # for i in range(cnt[1]):
        #     nums[cur+i] = 1
        # cur += cnt[1]
        # for i in range(cnt[2]):
        #     nums[cur+i] = 2

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        l = 0 # the idx for next 0 to be placed
        r = len(nums)-1 # the idx for the next 2 to be placed
        i = 0

        while True:
            if i > r:
                break
            
            if nums[i] == 0:
                swap(l, i)
                l += 1
                i += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
            else:
                i += 1