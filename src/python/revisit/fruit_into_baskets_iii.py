# https://leetcode.com/problems/fruits-into-baskets-iii

from typing import List
import math


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        rtn = math.ceil(math.sqrt(n))
        local_max = [-1] * rtn
        for i in range(rtn):
            for j in range(rtn):
                idx = i * rtn + j
                if idx >= n:
                    break
                local_max[i] = max(local_max[i], baskets[idx])

        unplaced = 0
        for f in fruits:
            placed = False

            for i in range(rtn):
                if local_max[i] < f:
                    continue

                # local_max[i] >= f
                local_max[i] = 0

                for j in range(rtn):
                    idx = i * rtn + j
                    if idx >= n:
                        break

                    if not placed and baskets[idx] >= f:
                        placed = True
                        baskets[idx] = -1

                    local_max[i] = max(local_max[i], baskets[idx])

                if placed:
                    break

            if not placed:
                unplaced += 1

        return unplaced
