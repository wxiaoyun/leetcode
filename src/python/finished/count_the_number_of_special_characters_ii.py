# https://leetcode.com/problems/count-the-number-of-special-characters-ii


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        lower_idx = [n] * 26
        upper_idx = [-1] * 26
        NOT_SPECIAL = -2

        for i, ch in enumerate(word):
            idx = ord(ch.lower()) - ord("a")
            if ch.islower():
                lower_idx[idx] = i
                if upper_idx[idx] >= 0 and i > upper_idx[idx]:
                    upper_idx[idx] = NOT_SPECIAL
            else:
                if upper_idx[idx] != NOT_SPECIAL:
                    upper_idx[idx] = i

        # for c in range(26):
        #     ch = chr(ord('a') + c)
        #     print(ch, lower_idx[c], upper_idx[c])

        return sum(1 if lower_idx[i] < upper_idx[i] else 0 for i in range(26))
