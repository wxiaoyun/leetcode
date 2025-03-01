# https://leetcode.com/problems/student-attendance-record-ii/

class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9+7

        # dp[i][j] = number of ways to have i absences and j curently consecutive lates
        dp = [[0]*3 for _ in range(2)]
        dp[0][0] = 1

        for _ in range(n):
            ndp = [[0]*3 for _ in range(2)]

            # P day
            ndp[0][0] = (dp[0][0] + dp[0][1] + dp[0][2])%mod
            ndp[1][0] = (dp[1][0] + dp[1][1] + dp[1][2])%mod

            # L day
            ndp[0][1] = dp[0][0]
            ndp[0][2] = dp[0][1]
            ndp[1][1] = dp[1][0]
            ndp[1][2] = dp[1][1]

            # A day
            ndp[1][0]+= (dp[0][0] + dp[0][1] + dp[0][2])%mod

            dp = ndp

        return sum([sum(s) for s in dp])%mod