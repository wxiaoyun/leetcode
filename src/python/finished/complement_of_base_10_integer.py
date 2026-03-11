# https://leetcode.com/problems/complement-of-base-10-integer


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 0
        i = 0
        while n:
            bit = n & 1
            ans |= (bit ^ 1) << i
            n >>= 1
            i += 1
        return ans
