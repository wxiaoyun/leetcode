from typing import List

# https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        even1 = len(nums1) % 2 == 0
        even2 = len(nums2) % 2 == 0
        
        res = 0
        if not even2:
            for n in nums1:
                res ^= n
        
        if not even1:
            for n in nums2:
                res ^= n
        return res
