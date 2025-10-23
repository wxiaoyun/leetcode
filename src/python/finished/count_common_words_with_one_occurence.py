# https://leetcode.com/problems/count-common-words-with-one-occurrence/

from typing import List
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1, freq2 = Counter(words1), Counter(words2)

        single_count = 0
        for w, f in freq1.items():
            if f != 1:
                continue
            if w not in freq2:
                continue
            if freq2[w] != 1:
                continue
            single_count += 1

        return single_count
