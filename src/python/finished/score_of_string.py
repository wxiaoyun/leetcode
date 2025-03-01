# https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:
        r = 0

        for i in range(1, len(s)):
            c0 = s[i-1]
            c1 = s[i]

            r += abs(ord(c0)-ord(c1))
        
        return r
        