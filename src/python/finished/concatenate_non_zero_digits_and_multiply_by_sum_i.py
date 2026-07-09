# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        l = 0
        stk = []
        sum = 0
        cur = n
        while cur > 0:
            d = cur % 10
            sum += d
            if d > 0:
                stk.append(d)
            cur //= 10
            l += 1

        x = 0
        for d in reversed(stk):
            x = x * 10 + d

        print(x, sum)
        return x * sum
