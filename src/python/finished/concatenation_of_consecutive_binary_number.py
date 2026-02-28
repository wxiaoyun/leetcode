# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # suppose we know the result of (n-1)

        # a % k = b
        # a = x * k + b
        # a << i = ((x * k) + b) << i
        # a << i = (x * k) << i + b << i
        # a << i = (x << i) * k + b << i

        def helper(n: int) -> int:
            if n == 1:
                return 1

            MOD = int(1e9) + 7

            res = helper(n - 1)

            bit_len = len(bin(n)) - 2

            return ((res << bit_len) + n) % MOD

        return helper(n)
