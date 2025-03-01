# https://leetcode.com/problems/grumpy-bookstore-owner

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        best = sum([0 if grumpy[i] == 1 else customers[i] for i in range(len(grumpy))])

        for i in range(minutes):
            if grumpy[i] == 1:
                best += customers[i]
        
        cur = best
        for i in range(minutes, len(grumpy)):
            j = i - minutes

            if grumpy[i] == 1:
                cur += customers[i]
            if grumpy[j] == 1:
                cur -= customers[j]
            
            best = max(best, cur)
        return best