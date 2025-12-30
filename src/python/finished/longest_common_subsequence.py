# https://leetcode.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # let dp[i][j] = LCS of s1[i] and s2[j]
        #
        # dp[i][j] = max of
        #   dp[i - 1][j]     if s1[i] != s2[j]
        #   dp[i][j - 1]     if s1[i] != s2[j]
        #   dp[i - 1][j - 1] if s1[i] == s2[j]

        # a b c d e
        #   ^
        # a   c   e

        s1 = text1
        s2 = text2
        n = len(s1)
        m = len(s2)
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + (dp[i - 1][j - 1] if min(i - 1, j - 1) >= 0 else 0)
                else:
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                    if j - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])

        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # dp[i][j] = longest subsequence of text1[:i] and text2[:j]
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            i_ch = text1[i]
            for j in range(n):
                j_ch = text2[j]

                if i_ch == j_ch:
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        dp[i][j] += dp[i - 1][j - 1]
                else:
                    if i > 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                    if j > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])

        return dp[m - 1][n - 1]
