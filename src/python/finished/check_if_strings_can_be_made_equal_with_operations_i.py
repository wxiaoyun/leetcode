from collections import Counter

# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return Counter(s1[i] for i in range(4) if i % 2 == 0) == Counter(
            s2[i] for i in range(4) if i % 2 == 0
        ) and Counter(s1[i] for i in range(4) if i % 2 == 1) == Counter(
            s2[i] for i in range(4) if i % 2 == 1
        )
