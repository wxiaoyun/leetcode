# https://leetcode.com/problems/longest-common-subsequence/


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
