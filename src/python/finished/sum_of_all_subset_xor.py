# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

import copy
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def gen(next: int, accum: List[List[int]]) -> List[List[int]]:
            cp = copy.deepcopy(accum)

            for l in cp:
                l.append(next)
            
            cp.extend(accum)
            return cp
        
        subsets = [[]]


        for n in nums:
            subsets = gen(n, subsets)
        
        def xor_sum(l: List[int]) -> int:
            res = 0

            for n in l:
                res = res^n
            
            return res
        
        return sum([xor_sum(l) for l in subsets])
