from collections import Counter

# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)

        if c1 != c2:
            return False
        
        diff_count = 0
        for i in range(len(s1)):
            ch1, ch2 = s1[i], s2[i]
            if ch1 != ch2:
                diff_count += 1
            
        return diff_count == 0 or diff_count == 2