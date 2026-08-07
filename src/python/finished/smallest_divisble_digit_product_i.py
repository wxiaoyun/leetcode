# https://leetcode.com/problems/smallest-divisible-digit-product-i


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(n: int) -> int:
            prod = 1
            while n > 0:
                prod *= n % 10
                n //= 10
            return prod

        cur = n
        while prod(cur) % t != 0:
            cur += 1
        return cur
