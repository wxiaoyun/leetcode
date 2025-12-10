from typing import List

# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        root_complexity = complexity[0]
        if min(complexity[1:]) <= root_complexity:
            return 0

        MOD = int(1e9) + 7
        ways = 1
        for i in range(1, len(complexity)):
            ways = (ways * i) % MOD
        return ways
