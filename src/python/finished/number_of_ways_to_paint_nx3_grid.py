from typing import List, Tuple

# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/


class Solution:
    def numOfWays(self, n: int) -> int:
        # Config = <int, int, int>
        # dp[n][c] = ways to paint n by 3 grid, given previous config c

        # let next_config(c) be all the valid next configs

        # dp[n][c] = sum over conf in next_config(c):
        #               dp[n - 1][conf]

        def compute(dp: dict, n: int, conf: Tuple[int, int, int]) -> int:
            if n == 0:
                return 1

            if conf in dp.setdefault(n, {}):
                return dp[n][conf]

            MOD = int(1e9) + 7
            ways = 0
            for nconf in next_config(conf):
                ways = (ways + compute(dp, n - 1, nconf)) % MOD

            dp[n][conf] = ways
            return ways

        cache = {}

        def next_config(conf: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
            if conf in cache:
                return cache[conf]

            def helper(builder: List[int], out: list):
                if len(builder) == 3:
                    a, b, c = builder
                    out.append((a, b, c))
                    return

                for color in range(3):
                    if color == conf[len(builder)]:
                        continue

                    if len(builder) > 0 and color == builder[-1]:
                        continue

                    builder.append(color)
                    helper(builder, out)
                    builder.pop()

                return

            out = []
            helper([], out)
            cache[conf] = out
            return out

        return compute({}, n, (-1, -1, -1))
