# https://leetcode.com/problems/subarray-sum-equals-k

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum = defaultdict(int)
        psum[0] = 1

        result = 0
        csum = 0
        for n in nums:
            csum += n
            need = csum - k
            result += psum[need]
            psum[csum] += 1
        
        return result