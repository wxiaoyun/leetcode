from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        plen = len(pref)
        return sum([1 if len(w) >= plen and w[:plen] == pref else 0 for w in words])
