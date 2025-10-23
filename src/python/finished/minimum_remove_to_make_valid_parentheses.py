from typing import List

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        include_char = [False] * len(s)
        bracket_stack: List[int] = []

        for i, ch in enumerate(s):
            if ch not in "()":
                include_char[i] = True
                continue

            if ch == "(":
                bracket_stack.append(i)
                continue

            # ch == ")":
            if len(bracket_stack) == 0:
                continue

            include_char[i] = True
            open_bracket_index = bracket_stack.pop()
            include_char[open_bracket_index] = True

        sbuilder = []
        for i in range(len(s)):
            if include_char[i]:
                sbuilder.append(s[i])

        return "".join(sbuilder)
