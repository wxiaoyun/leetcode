# https://leetcode.com/problems/longest-ideal-subsequence


# O(26N)
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        S = len(s)
        dist = [0] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            best = dist[idx]
            for jdx in range(max(0, idx - k), min(26, idx + k + 1)):
                best = max(best, dist[jdx] + 1)
            dist[idx] = best

        return max(dist)


# O(N^2) TLE
class Solution2:
    def longestIdealString(self, s: str, k: int) -> int:
        S = len(s)
        dp = [1] * S

        for i, ch in enumerate(s):
            for j in range(i):
                jch = s[j]

                if abs(ord(jch) - ord(ch)) <= k:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
