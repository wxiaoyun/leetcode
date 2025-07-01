# https://leetcode.com/problems/find-the-original-typed-string-i


class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 1
        cur, cnt = "", 0
        for ch in word:
            if ch == cur:
                cnt += 1
            else:
                total += cnt
                cur = ch
                cnt = 0
        if cur != "":
            total += cnt
        return total
