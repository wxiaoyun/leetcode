from typing import List

# https://leetcode.com/problems/sequential-digits/


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        cur = low
        while cur <= high:
            ndigits = len(str(cur))
            jump = 0
            start = 0
            for i in range(ndigits):
                jump = jump * 10 + 1
                start = start * 10 + i + 1
            # print(cur, ndigits, jump, start)

            bound = min(high + 1, 10 ** (ndigits + 1))
            n = start
            while n < bound:
                if n >= low:
                    ans.append(n)
                n += jump
                if n % 10 == 0:
                    break
            cur = 10**ndigits
            # print(cur)
        return ans
