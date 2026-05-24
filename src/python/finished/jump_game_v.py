from typing import List

# https://leetcode.com/problems/jump-game-v


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        ls = [(n, i) for i, n in enumerate(arr)]
        ls.sort()
        # print(ls)

        dp = {}
        for n, i in ls:
            dp[i] = 1

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
        # print(dp)
        return max(dp.values())
