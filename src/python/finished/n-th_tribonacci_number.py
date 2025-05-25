from collections import deque

# https://leetcode.com/problems/n-th-tribonacci-number


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = deque([0, 1, 1])
        if n < 2:
            return dp[n]

        cur = 2
        while cur < n:
            dp.append(sum(dp))
            dp.popleft()
            cur += 1

        return dp[-1]
