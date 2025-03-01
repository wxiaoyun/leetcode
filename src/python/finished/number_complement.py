# https://leetcode.com/problems/number-complement/


class Solution:
    def findComplement(self, num: int) -> int:
        bits = []

        while num > 0:
            bits.append(num % 2)
            num = num // 2

        res = 0
        for b in reversed(bits):
            res *= 2
            res += 1 if b == 0 else 0
        return res
