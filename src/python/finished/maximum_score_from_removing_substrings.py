# https://leetcode.com/problems/maximum-score-from-removing-substrings/


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = "a", "b"
        ascore, bscore = x, y
        if x < y:
            a, b = "b", "a"
            ascore, bscore = y, x

        score = 0
        stack = []
        for ch in s:
            if ch == b and len(stack) > 0 and stack[-1] == a:
                stack.pop()
                score += ascore
                continue

            stack.append(ch)

        stack2 = []
        for ch in stack:
            if ch == a and len(stack2) > 0 and stack2[-1] == b:
                stack2.pop()
                score += bscore
                continue

            stack2.append(ch)

        return score
