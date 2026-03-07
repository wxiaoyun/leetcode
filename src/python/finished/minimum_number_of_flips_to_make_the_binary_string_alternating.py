# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/


class Solution:
    def minFlips(self, s: str) -> int:

        # observation 1:
        # - type 1 operation never changes the number of 1s and 0s,
        #   so if the number of 1s and 0s are unequal, we need `abs(count(1), count(0)) // 2` type 2 operations
        # - type 1 operation essentially changes where the binary string starts (with wrap around.
        #   there can be at most (n - 1) meaningful type 1 operations
        #

        NO_FLIP = 0
        FLIP = 1

        def compute(dp: dict, s: str, i: int, prev_flip: int, wildcard: int) -> int:
            if i >= len(s):
                return 0

            key = (i, prev_flip, wildcard)
            if key in dp:
                return dp[key]

            INF = 1 << 31
            best = INF

            prev = int(s[i - 1]) ^ prev_flip
            cur = int(s[i])

            if prev == cur:
                if wildcard > 0:
                    best = min(best, compute(dp, s, i + 1, NO_FLIP, wildcard - 1))
                best = min(best, 1 + compute(dp, s, i + 1, FLIP, wildcard))
            else:
                best = min(best, compute(dp, s, i + 1, NO_FLIP, wildcard))

            dp[key] = best
            return best

        wildcard = 0
        if len(s) % 2 == 1:
            wildcard = 1

        dp = {}
        return min(
            compute(dp, s, 1, NO_FLIP, wildcard),
            1 + compute(dp, s, 1, FLIP, wildcard),
        )
