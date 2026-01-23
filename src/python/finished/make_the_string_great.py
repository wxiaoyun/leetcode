# https://leetcode.com/problems/make-the-string-great/


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if (
                stack
                and stack[-1].upper() == ch.upper()
                and (stack[-1].isupper() ^ ch.isupper())
            ):
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
