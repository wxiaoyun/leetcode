from typing import List

# https://leetcode.com/problems/jump-game-v


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        ls = [(n, i) for i, n in enumerate(arr)]
        ls.sort()
        # print(ls)

        best = 1
        dp = [1] * len(arr)
        for n, i in ls:
            for j in range(i - 1, max(-1, i - d - 1), -1):
                jn = arr[j]
                if jn >= n:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
            for j in range(i + 1, min(len(arr), i + d + 1)):
                jn = arr[j]
                if jn >= n:
                    break
                dp[i] = max(dp[i], dp[j] + 1)
            best = max(best, dp[i])
        # print(dp)
        return best
