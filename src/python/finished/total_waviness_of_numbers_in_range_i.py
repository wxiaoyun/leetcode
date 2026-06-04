# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        dp = {}

        def waviness(nstr: str) -> int:
            if len(nstr) < 3:
                return 0
            if nstr in dp:
                return dp[nstr]

            half = len(nstr) // 2

            nwav = 0
            nwav += waviness(nstr[:half])
            nwav += waviness(nstr[half:])

            l, r = half - 1, half

            centers = [l, r]
            for c in centers:
                l, m, r = c - 1, c, c + 1
                if not l >= 0 or not r < len(nstr):
                    continue

                is_valley = int(nstr[l]) > int(nstr[m]) and int(nstr[m]) < int(nstr[r])
                is_peak = int(nstr[l]) < int(nstr[m]) and int(nstr[m]) > int(nstr[r])
                if is_valley or is_peak:
                    nwav += 1

            dp[nstr] = nwav
            return nwav

        return sum(waviness(str(n)) for n in range(num1, num2 + 1))
