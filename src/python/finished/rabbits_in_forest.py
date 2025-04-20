from typing import Counter, List

# https://leetcode.com/problems/rabbits-in-forest


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)

        min_total = 0
        for n, f in cnt.items():
            n = n + 1
            # 1 ... n -> 1
            # n + 1 ... 2n -> 2
            min_total += n * ((f - 1) // n + 1)
        return min_total
