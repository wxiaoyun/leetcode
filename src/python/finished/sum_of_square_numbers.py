# https://leetcode.com/problems/sum-of-square-numbers/

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # for i in range(int(math.sqrt(c))+1):
        #     a=i
        #     b=(math.sqrt(c-a**2))//1
        #     if a**2 + b**2 == c:
        #         return True
        
        # return False

        l, r = 0, int(math.sqrt(c))

        while l <= r:
            _sum = l**2+r**2
            if _sum == c:
                return True
            
            if _sum < c:
                l+=1
                continue
            
            if _sum > c:
                r-=1
                continue
        
        return False