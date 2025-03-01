# https://leetcode.com/problems/subarray-sums-divisible-by-k/

from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # psum = [0]

        # for n in nums:
        #     psum.append(n+psum[-1])
        
        # def sumof(fr:int, to: int):
        #     return psum[to] - psum[fr]
        
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)+1):
        #        if sumof(j,i)%k == 0:
        #         count+=1
        # return count 
        
        prem = [0]

        for n in nums:
            prem.append((n+prem[-1])%k)
        
        cnt = defaultdict(int)

        for r in prem:
            cnt[r] += 1
        
        result = 0
        for c in cnt.values():
            result += (c*(c-1))//2
        return result