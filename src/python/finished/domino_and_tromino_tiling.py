# https://leetcode.com/problems/domino-and-tromino-tiling/description


class Solution:
    def numTilings(self, n: int) -> int:
        ways = {}
        ways[(1, True)] = 1
        ways[(1, False)] = 0
        ways[(2, True)] = 2
        ways[(2, False)] = 1

        def compute(ways: dict, n: int, filled: bool, MOD=(10**9) + 7) -> int:
            if n <= 0:
                return True

            key = (n, filled)
            if key in ways:
                return ways[key]

            total = 0

            if not filled:
                total += compute(ways, n - 1, False)
                total += compute(ways, n - 2, True)
                total %= MOD
            else:
                total += compute(ways, n - 1, True)
                total += compute(ways, n - 1, False) * 2
                total += compute(ways, n - 2, True)
                total %= MOD

            ways[key] = total
            return total

        res = compute(ways, n, True)
        return res
