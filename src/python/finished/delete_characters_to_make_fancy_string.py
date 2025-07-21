# https://leetcode.com/problems/delete-characters-to-make-fancy-string


class Solution:
    def makeFancyString(self, s: str) -> str:
        prev, pcnt = "", 0
        res = []
        for c in s:
            if c == prev:
                if pcnt < 2:
                    pcnt += 1
                else:
                    continue
            else:
                prev = c
                pcnt = 1

            res.append(c)
        return "".join(res)


class Solution:
    def makeFancyString(self, s: str) -> str:
        builder = [s[i] for i in range(min(2, len(s)))]
        for i in range(2, len(s)):
            if (s[i]) * 3 == s[i - 2 : i + 1]:
                continue
            builder.append(s[i])
        return "".join(builder)
