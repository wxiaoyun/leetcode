# https://leetcode.com/problems/relative-sort-array

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        fn = {}
        largest = -float('inf')
        for idx, n in enumerate(arr2):
            fn[n] = idx
            largest = max(largest, n)
        
        arr1.sort(key=lambda x: fn[x] if x in fn else 2000 + x)
        return arr1