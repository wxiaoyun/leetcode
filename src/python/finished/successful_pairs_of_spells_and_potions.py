# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        def bin_search(arr: list, target: int) -> int:
            # return the left_most index such that arr[index] >= target
            l, r = 0, len(arr)
            ans = r

            while l < r:
                m = l + (r - l) // 2
                mval = arr[m]

                if mval >= target:
                    ans = m
                    r = m
                else:
                    l = m + 1

            return ans

        n = len(spells)
        m = len(potions)

        pairs = [0] * n
        potions = sorted(potions)

        for i, spell in enumerate(spells):
            # a * b >= c
            # b >= c / a
            pairs[i] = m - bin_search(potions, success / spell)

        return pairs
