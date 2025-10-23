# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(ch) for ch in s]
        bound = len(digits) - 1

        while bound >= 2:
            for i in range(bound):
                digits[i] = (digits[i] + digits[i + 1]) % 10
            bound -= 1

        return digits[0] == digits[1]
