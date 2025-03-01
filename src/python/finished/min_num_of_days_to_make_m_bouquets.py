# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1
        
        def canMakeBouquets(days: int) -> bool:
            remaining = m
            i = 0
            while i < len(bloomDay):
                count = 0
                while i < len(bloomDay) and count < k:
                    if bloomDay[i]-days <= 0:
                        count+=1
                        i+=1
                    else:
                        i+=1
                        break
                if count == k:
                    remaining-=1
                if remaining == 0:
                    return True
            return False
        
        l, r = min(bloomDay), max(bloomDay)

        while l < r:
            mid = (l+r)//2
            if canMakeBouquets(mid):
                r = mid
            else:
                l = mid+1
        return l
        
