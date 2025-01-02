from typing import List

# https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(list("aeiou"))
        psum = [0]

        for w in words:
            cnt = psum[-1]
            if w[0] in vowels and w[-1] in vowels:
                cnt += 1
            psum.append(cnt)
        
        ans = [None] * len(queries)
        for i, (ql, qr) in enumerate(queries):
            ans[i] = psum[qr+1] - psum[ql]
        return ans