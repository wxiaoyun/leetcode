# https://leetcode.com/problems/interleaving-string/


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        # dp[i][j] = possible to form s3[:i+j] from s1[:i] and s2[:j]
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # dp[i][j] iff
        #    dp[i - 1][j] == True and s1[i - 1] == s3[i + j - 1]
        # or dp[i][j - 1] == True and s2[j - 1] == s3[i + j - 1]

        for i in range(n + 1):
            for j in range(m + 1):
                if i - 1 >= 0:
                    dp[i][j] = dp[i][j] or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                if j - 1 >= 0:
                    dp[i][j] = dp[i][j] or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        # dp[i][j]:
        # - Does s1[..i] and s2[..j] form s3[..i + j]

        # dp[i][j] == True:
        # 1. if dp[i][j - 1] == True and s2[j - 1] == s3[i + j - 1]
        # 2. if dp[i - 1][j] == True and s1[i - 1] == s3[i + j - 1]

        dp = [False] * (m + 1)
        tmp = [False] * (m + 1)
        dp[0] = True

        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, n + 1):
            s1_ch = s1[i - 1]
            tmp[0] = dp[0] and s1_ch == s3[i - 1]
            for j in range(1, m + 1):
                s2_ch = s2[j - 1]
                s3_ch = s3[i + j - 1]

                use_s1 = dp[j] and s1_ch == s3_ch
                use_s2 = tmp[j - 1] and s2_ch == s3_ch
                tmp[j] = use_s1 or use_s2

            tmp, dp = dp, tmp

        return dp[-1]
