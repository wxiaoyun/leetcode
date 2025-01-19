# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        free = []

        for i in range(len(s)):
            ch = s[i]
            is_locked = locked[i] == "1"

            if not is_locked:
                free.append(i)
                continue

            if ch == "(":
                stack.append(i)
                continue

            # ch == ")"
            if stack:
                stack.pop()
                continue

            # stack empty
            if free:
                free.pop()  # consume a free bracket for "("
                continue

            return False

        while stack and free and stack[-1] < free[-1]:
            stack.pop()
            free.pop()  # use the free backet for ")"

        return len(stack) == 0

    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        free = []
        brackets = []

        for i, ch in enumerate(s):
            if locked[i] == "0":
                free.append(i)
                continue

            if ch == "(":
                brackets.append(i)
                continue

            # chr == ')'
            if brackets:
                brackets.pop()
                continue

            # count == 0
            if free:
                free.pop()
                continue

            return False

        while brackets and free and brackets[-1] < free[-1]:
            brackets.pop()
            free.pop()

        if brackets:
            return False

        return True
