# https://leetcode.com/problems/number-of-1-bits/


table = [0] * (1 << 8)
for i in range(1 << 8):
    table[i] = (i & 1) + table[i >> 1]


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += table[n & 0b11111111]
            n >>= 8
        return ans
