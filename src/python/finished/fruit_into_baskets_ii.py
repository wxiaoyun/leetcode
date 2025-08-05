# https://leetcode.com/problems/fruits-into-baskets-ii

from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0

        for f in fruits:
            placed = False
            for i in range(len(baskets)):
                if baskets[i] < 0:
                    continue

                if baskets[i] >= f:
                    baskets[i] = -1
                    placed = True
                    break

            if not placed:
                unplaced += 1

        return unplaced
