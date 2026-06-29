from typing import List

# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 if pat in word else 0 for pat in patterns)
