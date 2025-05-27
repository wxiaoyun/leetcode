# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        ms = n // m
        total -= ms * (2 * m + (ms - 1) * m)
        return total
