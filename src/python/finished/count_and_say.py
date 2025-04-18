# https://leetcode.com/problems/count-and-say


class Solution:
    def countAndSay(self, n: int) -> str:
        def compress(s: str) -> str:
            res = []

            prev = s[0]
            count = 1
            for ch in s[1:]:
                if prev == ch:
                    count += 1
                    continue

                res.append(str(count))
                res.append(prev)
                count = 1
                prev = ch

            res.append(str(count))
            res.append(s[-1])
            return "".join(res)

        res = "1"
        for _ in range(n - 1):
            res = compress(res)
        return res
