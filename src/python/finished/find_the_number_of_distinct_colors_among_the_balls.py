from typing import List

# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        cfreq = {}
        b2c = {}
        ans = []

        for b, c in queries:
            # update the color of b
            if b in b2c:
                prevc = b2c[b]
                if cfreq[prevc] == 1:
                    del cfreq[prevc]
                else:
                    cfreq[prevc] -= 1
            b2c[b] = c

            if c not in cfreq:
                cfreq[c] = 0
            cfreq[c] += 1

            ans.append(len(cfreq))
        
        return ans

