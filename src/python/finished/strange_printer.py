# https://leetcode.com/problems/strange-printer


class Solution:
    def strangePrinter(self, s: str) -> int:
        N = len(s)
        dp = {}

        def compute(i: int, j: int) -> int:
            if i > j:
                return 0

            key = (i, j)
            if key in dp:
                return dp[key]

            res = 1 + compute(i + 1, j)  # print 1 character sequentially

            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    res = min(res, compute(i, k - 1) + compute(k + 1, j))
            dp[key] = res
            return res

        return compute(0, N - 1)


class Solution:
    def strangePrinter(self, s: str) -> int:
        # deduplicate consecutive identical characters
        chars = []
        prev = ""
        for ch in s:
            if ch == prev:
                continue
            chars.append(ch)
            prev = ch
        N = len(chars)

        dp = {}

        def compute(start: int, end: int) -> int:
            if start > end:
                return 0

            key = (start, end)
            if key in dp:
                return dp[key]

            # Case 1: print characters 1 by 1
            res = 1 + compute(start + 1, end)

            # Case 2: try to find similar characters and avoid printing them again
            for mid in range(start + 1, end + 1):
                if not chars[start] == chars[mid]:
                    continue

                res = min(
                    res,
                    compute(start, mid - 1) + compute(mid + 1, end),
                    # print colors between start and mid - 1, print everything after mid
                    # The first printed part starts with colors[start], so we get colors[mid] for free
                )

            dp[key] = res
            return res

        return compute(0, N - 1)
