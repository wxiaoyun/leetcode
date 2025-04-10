# https://leetcode.com/problems/count-the-number-of-powerful-integers/description


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        snum = int(s)
        if snum > finish:
            return 0

        def calculate(n: str) -> int:
            if len(n) < len(s):
                return 0
            if len(n) == len(s):
                return 1 if n >= s else 0

            slen = len(s)
            nprefix = n[:-slen]

            count = 0
            excess = False
            for d in nprefix:
                nd = int(d) if not excess else limit
                if limit < nd:
                    excess = True
                    nd = limit
                count = count * (limit + 1) + nd

            nsuffix = n[-slen:]
            if nsuffix >= s or excess:
                count += 1
            return count

        return calculate(str(finish)) - calculate(str(start - 1))
