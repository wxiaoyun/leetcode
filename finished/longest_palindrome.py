# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # def expand(i: int, j: int) -> int:
        #     if i < 0 or j >= len(s):
        #         return j-i
            
        #     if s[i] != s[j]:
        #         return j-(i+1)
            
        #     return expand(i-1, j+1)
        
        # _max = 1
        # for i in range(1, len(s)):
        #     _max = max(_max, expand(i-1,i))
        #     _max = max(_max, expand(i,i))
        
        # return _max

        c = Counter(s)

        l = 0
        odd = False
        for c, f in c.items():
            if f % 2 == 1:
                odd = True
            
            l+= f//2*2
        
        if odd:
            l+=1
        return l