from typing import List
from collections import Counter

# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        freqs = [Counter(w) for w in words]

        ans = [words[0]]
        for i in range(1, n):
            if freqs[i - 1] == freqs[i]:
                continue
            ans.append(words[i])
        return ans
