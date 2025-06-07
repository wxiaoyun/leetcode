# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars


class Solution:
    def clearStars(self, s: str) -> str:
        def ordd(ch: str) -> int:
            return ord(ch) - ord("a")

        count = [[] for _ in range(26)]
        to_del = set()
        for i in range(len(s)):
            ch = s[i]

            if ch != "*":
                ch_ord = ordd(ch)
                count[ch_ord].append(i)
                continue

            for ls in count:
                if len(ls) == 0:
                    continue
                to_del.add(ls.pop())
                break

        res = []
        for i, ch in enumerate(s):
            if i in to_del or ch == "*":
                continue
            res.append(ch)
        return "".join(res)
