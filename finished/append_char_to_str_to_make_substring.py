# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_ptr = 0
        for c in s:
            if t_ptr >= len(t):
                return 0

            # print(c, t[t_ptr], t_ptr)
            
            if c == t[t_ptr]:
                t_ptr+=1
        
        return len(t)-t_ptr