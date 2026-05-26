# https://leetcode.com/problems/count-the-number-of-special-characters-i/


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        UPPER = 1 << 0
        LOWER = 1 << 1
        ALL = UPPER | LOWER
        check = [0] * 26
        for ch in word:
            idx = ord(ch.lower()) - ord("a")
            if ch.isupper():
                check[idx] |= UPPER
            else:
                check[idx] |= LOWER
        return sum(1 if v == ALL else 0 for v in check)
