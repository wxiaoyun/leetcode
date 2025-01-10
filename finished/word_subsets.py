from collections import Counter
from typing import Dict, List

# https://leetcode.com/problems/word-subsets/

class Solution:
    # Time: O(n + m)
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wd1 = [Counter(w) for w in words1]
        wd2 = [Counter(w) for w in words2]

        word2 = {}
        for d in wd2:
            for ch, cnt in d.items():
                if ch not in word2:
                    word2[ch] = 0
                word2[ch] = max(word2[ch], cnt)

        res = []
        for i, d1 in enumerate(wd1):
            universal = True
            for ch, cnt in word2.items():
                if ch not in d1 or d1[ch] < cnt:
                    universal = False
                    break

            if universal:
                res.append(words1[i])

        return res

    # Time: O(nm)
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def process_word(w: str) -> Dict[str, int]:
            res = {}
            for ch in w:
                if ch not in res:
                    res[ch] = 0
                res[ch] += 1
            return res

        wd1 = [process_word(w) for w in words1]
        wd2 = [process_word(w) for w in words2]

        res = []
        for i, d1 in enumerate(wd1):
            universal = True
            for d2 in wd2:
                for ch, cnt in d2.items():
                    if ch not in d1 or d1[ch] < cnt:
                        universal = False
                        break
            if universal:
                res.append(words1[i])
        return res
