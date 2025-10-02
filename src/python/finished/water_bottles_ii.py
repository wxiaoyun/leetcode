# https://leetcode.com/problems/water-bottles-ii/


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        n_drank = 0
        n_empty = 0
        n_full = numBottles
        while n_full:
            n_drank += n_full
            n_empty += n_full
            n_full = 0

            while n_empty >= numExchange:
                n_empty -= numExchange
                n_full += 1
                numExchange += 1

        return n_drank
