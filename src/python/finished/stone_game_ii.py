# https://leetcode.com/problems/stone-game-ii/


from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        suffix_sum = [0] * (len(piles) + 1)
        for i in reversed(range(len(piles))):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        dp = {}

        def compute(i: int, m: int = 1) -> int:
            if i >= len(piles):
                return 0

            key = (i, m)
            if key in dp:
                return dp[key]

            best = 0
            takes = 0
            for x in range(2 * m):
                j = i + x
                if j >= len(piles):
                    break
                takes += piles[j]
                opp_take = compute(j + 1, max(m, x + 1))
                me_take = suffix_sum[j + 1] - opp_take
                best = max(best, takes + me_take)

            dp[key] = best
            return best

        return compute(0)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        prefix_sum = [0] * (N + 1)
        for i, p in enumerate(piles):
            prefix_sum[i + 1] = prefix_sum[i] + p
        # prefix_sum[i] == sum(piles[:i])

        # alice[i, M] = max(
        #   for x in range(i + 1, i + 2M):
        #    piles[i:x] - bob(x)
        # )

        dp = {}

        def compute(i: int, M: int) -> int:
            if i >= N:
                return 0

            key = (i, M)
            if key in dp:
                return dp[key]

            best = 0
            for x in range(1, 2 * M + 1):
                if x + i > N:
                    break

                taken = prefix_sum[i + x] - prefix_sum[i]
                remaining = prefix_sum[-1] - prefix_sum[i + x]
                opponent_taken = compute(i + x, max(M, x))
                best = max(best, taken + remaining - opponent_taken)
            dp[key] = best
            return best

        return compute(0, 1)

    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        postfix_sum = [piles[-1]] * N
        for i in reversed(range(N - 1)):
            postfix_sum[i] = postfix_sum[i + 1] + piles[i]
        dp = {}

        def helper(M: int, up_to: int) -> int:
            if up_to >= N:
                return 0
            if up_to + 2 * M > N:
                return postfix_sum[up_to]
            key = (M, up_to)
            if key in dp:
                return dp[key]

            best = float("inf")
            for X in range(1, min(2 * M + 1, N)):
                until = up_to + X
                taken = sum(piles[up_to:until])
                # minimise what the opponent gets -> maximise our own winning
                best = min(best, helper(max(M, X), until))
            res = postfix_sum[up_to] - best
            dp[key] = res
            return res

        return helper(1, 0)
