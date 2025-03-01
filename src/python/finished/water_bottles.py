# https://leetcode.com/problems/water-bottles

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        full = numBottles
        empty = 0
        while True:
            res += full
            empty += full
            full = empty // numExchange
            empty = empty % numExchange
            if full + empty < numExchange:
                res += full
                break
            
        return res
        