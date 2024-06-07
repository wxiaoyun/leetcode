# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        def helper(s: str, i: int, c: str, accum: int) -> int:
            if i >= len(s):
                return accum
            
            next_c = '0' if c == '1' else '1'

            if s[i] != c:
                return helper(s, i+1, next_c, accum+1)
            else:
                return helper(s, i+1, next_c, accum)
            
        return min(
            helper(s, 0, '1', 0),
            helper(s, 0, '0', 0)
        )
        
