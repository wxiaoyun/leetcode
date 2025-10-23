# https://leetcode.com/problems/valid-word-abbreviation/


class Cursor:
    def __init__(self, s: str):
        self.s = s
        self.i = 0

    def has_next(self) -> bool:
        return self.i < len(self.s)

    def next_abbr_num(self) -> bool:
        return self.s[self.i].isnumeric()

    def next_chars(self) -> str:
        builder = []

        while self.i < len(self.s):
            ch = self.s[self.i]
            if ch.isnumeric():
                break
            builder.append(ch)
            self.i += 1

        return "".join(builder)

    def next_num(self) -> int:
        builder = 0

        while self.i < len(self.s):
            ch = self.s[self.i]
            if not ch.isnumeric():
                break
            if ch == "0" and builder == 0:
                return float("inf")
            builder *= 10
            builder += int(ch)
            self.i += 1

        return builder


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        cursor = Cursor(abbr)

        i = 0
        while i < len(word):
            if not cursor.has_next():
                return False

            if cursor.next_abbr_num():
                i += cursor.next_num()
            else:
                chars = cursor.next_chars()

                for ch in chars:
                    if not i < len(word):
                        return False

                    if ch != word[i]:
                        return False

                    i += 1

        return i == len(word) and cursor.i == len(cursor.s)
