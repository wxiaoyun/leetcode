# https://leetcode.com/problems/remove-all-occurrences-of-a-substring

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        plen = len(part)
        plist = list(part)
        
        stack = []
        for ch in s:
            stack.append(ch)

            if len(stack) < plen:
                continue
            
            if plist == stack[-plen:]:
                stack = stack[:-plen]
        
        return "".join(stack)