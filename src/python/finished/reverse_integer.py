# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        if is_neg:
            x = -x

        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x //= 10

        if is_neg:
            ans = -ans
        return ans if ans >= -(1 << 31) and ans <= (1 << 31) - 1 else 0
