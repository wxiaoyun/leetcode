from typing import List

# https://leetcode.com/problems/weighted-word-mapping/


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        mapping = list(reversed("abcdefghijklmnopqrstuvwxyz"))

        res = [""] * len(words)
        for i, w in enumerate(words):
            idx = sum(weights[ord(ch) - ord("a")] for ch in w) % 26
            res[i] = mapping[idx]

        return "".join(res)
