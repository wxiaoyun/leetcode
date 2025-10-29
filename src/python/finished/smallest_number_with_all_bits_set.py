# https://leetcode.com/problems/smallest-number-with-all-bits-set/


class Solution:
    def smallestNumber(self, n: int) -> int:
        bits = len(bin(n)) - 2
        return (1 << bits) - 1