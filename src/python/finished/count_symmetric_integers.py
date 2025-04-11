# https://leetcode.com/problems/count-symmetric-integers


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for n in range(low, high + 1):
            nstr = str(n)

            if len(nstr) % 2 == 1:
                continue
            hlen = len(nstr) // 2
            if sum([int(d) for d in nstr[:hlen]]) == sum([int(d) for d in nstr[hlen:]]):
                count += 1

        return count
