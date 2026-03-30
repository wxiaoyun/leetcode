from collections import Counter

# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # e1 o1 e2 o2 e3
        # e2 o1 e1 o2 e3
        # e2 o1 e3 o2 e1
        # e3 o1 e2 o2 e1

        # observations:
        # 1. Operations can only affect indices with the same parity (even or odd)
        # 2. It is possible to swap two indices with the same parity without changing over indices

        n = len(s1)
        assert n == len(s2)

        s1_evens = Counter(s1[i] for i in range(n) if i % 2 == 0)
        s2_evens = Counter(s2[i] for i in range(n) if i % 2 == 0)
        if s1_evens != s2_evens:
            return False

        s1_odds = Counter(s1[i] for i in range(n) if i % 2 == 1)
        s2_odds = Counter(s2[i] for i in range(n) if i % 2 == 1)
        if s1_odds != s2_odds:
            return False

        return True
