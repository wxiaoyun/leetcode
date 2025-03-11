# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = {c: 0 for c in "abc"}
        total = 0
        l = 0
        for r, ch in enumerate(s):
            cnt[ch] += 1

            lch = s[l]
            while min(cnt.values()) > 0 and cnt[lch] > 1:
                cnt[lch] -= 1
                l += 1
                lch = s[l]
            
            if min(cnt.values()) > 0:
                total += l + 1
        
        return total