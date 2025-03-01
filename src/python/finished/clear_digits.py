# https://leetcode.com/problems/clear-digits

class Solution:
    def clearDigits(self, s: str) -> str:
        chars = []
        for i, ch in enumerate(s):
            if not ch.isdigit():
                chars.append(ch)
                continue
            
            if not chars:
                chars.extend(s[i:])
                break
            
            chars.pop()
        
        return "".join(chars)