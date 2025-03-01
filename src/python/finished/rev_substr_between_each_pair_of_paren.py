# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses

from typing import Tuple


class Solution:
    def reverseParentheses(self, s: str) -> str:

        def extract(i: int) -> Tuple[str, int]:
            builder = []
            
            j = i
            while j < len(s):
                c = s[j]
                if c == ")":
                    builder.reverse()
                    rv = "".join(builder)
                    return (rv, j+1) # Skip ')'
                elif c == "(":
                    rv, n_idx = extract(j+1) # Skip '('
                    builder.extend([*rv])
                    j = n_idx
                else:
                    builder.append(c)
                    j += 1
            
            rv = "".join(builder)
            return (rv, j+1)

        rv, _ = extract(0)
        return rv