# https://leetcode.com/problems/intersection-of-two-arrays-ii

from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for n in nums1:
            d1[n] += 1
        for n in nums2:
            d2[n] += 1
        
        lg, sm = None, None
        if len(d1) > len(d2):
            lg = d1
            sm = d2
        else:
            lg = d2
            sm = d1
        
        res = []
        for k, v in lg.items():
            count = min(v, sm[k])
            res.extend([k]*count)
        return res
        