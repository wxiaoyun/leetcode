# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        i = len(s)-1
        while i >= 1:
            cur = carry + (0 if s[i] == '0' else 1)
            carry = 0

            if cur > 1:
                carry = 1
                cur = 0

            if cur == 0:
                steps += 1
            else:
                steps += 2 # (1) odd -> add. (2) divide by 2
                carry += 1
            i-=1
        
        cur = carry + (0 if s[0] == '0' else 1)
        if cur == 1:
            return steps
        elif cur == 2:
            return steps+1