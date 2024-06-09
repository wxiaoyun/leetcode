# https://leetcode.com/problems/continuous-subarray-sum

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # psum = [0]

        # for n in nums:
        #     psum.append(n+psum[-1])
        
        # def sumof(fr: int, to: int) -> int:
        #     return psum[to] - psum[fr]

        # for i in range(len(nums)):
        #     for j in range(i+2, len(nums)+1):
        #         if sumof(j, i) % k == 0:
        #             return True
        
        # return False
        
        rmd = {
            0: -1
        }
        rmd_total = 0

        for i, n in enumerate(nums):
            rmd_total = (rmd_total+n)%k

            if rmd_total not in rmd:
                rmd[rmd_total] = i
            elif i - rmd[rmd_total] > 1:
                return True
            
        return False