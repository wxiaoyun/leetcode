# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sm, prod = 0, 1
        cur = n
        while cur != 0:
            digit = cur % 10
            cur //= 10
            sm += digit
            prod *= digit
        return n % (sm + prod) == 0
