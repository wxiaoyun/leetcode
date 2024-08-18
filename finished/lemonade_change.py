# https://leetcode.com/problems/lemonade-change

from typing import DefaultDict, List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = DefaultDict(int)

        def try_change(bill: int) -> bool:
            while bill >= 10:
                if change[10] <= 0:
                    break
                change[10] -= 1
                bill -= 10

            while bill >= 5:
                if change[5] <= 0:
                    break
                change[5] -= 1
                bill -= 5

            return bill == 0

        for b in bills:
            change[b] += 1
            if try_change(b - 5):
                continue
            else:
                return False
        return True
