# https://leetcode.com/problems/number-of-people-aware-of-a-secret/


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        nsharing = [0] * (n + 1)
        nsharing[1] = 1
        nsharing[2] = -1

        nforget = [0] * (n + 1)

        MOD = int(1e9 + 7)
        cur_sharing = 0
        cur = 0
        for day in range(1, n + 1):
            cur_sharing += nsharing[day]
            cur = (cur + cur_sharing - nforget[day]) % MOD

            if day + delay <= n:
                nsharing[day + delay] += cur_sharing
            if day + forget <= n:
                nsharing[day + forget] -= cur_sharing
                nforget[day + forget] += cur_sharing

        return cur
