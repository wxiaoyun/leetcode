# https://leetcode.com/problems/maximum-score-from-removing-substrings

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if len(s) < 2:
            return 0

        def score_of(s: str) -> int:
            if s=="ab":
                return x
            elif s=="ba":
                return y
            else:
                return 0

        bigger =  "ab" if x > y else "ba"
        smaller = "ba" if x > y else "ab"
        stack = []
        score = 0

        for c in s:
            if not stack:
                stack.append(c)
                continue
            
            if stack[-1]+c == bigger:
                popped = stack.pop()
                score += score_of(popped+c)
            else:
                stack.append(c)
        
        remaining = stack
        stack = []

        for c in remaining:
            if not stack:
                stack.append(c)
                continue
            
            if stack[-1]+c == smaller:
                popped = stack.pop()
                score += score_of(popped+c)
            else:
                stack.append(c)
        
        return score