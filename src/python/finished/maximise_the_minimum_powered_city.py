from typing import List


# https://leetcode.com/problems/maximize-the-minimum-powered-city/


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def possible(stations: List[int], r: int, k: int, target: int) -> bool:
            n = len(stations)
            delta = [0] * (n + 1)

            for i in range(n):
                cnt = stations[i]
                lo = max(0, i - r)
                hi = min(n, i + r + 1)
                delta[lo] += cnt
                delta[hi] -= cnt

            cur_pow = 0
            for i in range(n):
                cur_pow += delta[i]

                dif = cur_pow - target  # negative if cur_pow < target
                if dif >= 0:
                    continue
                if k + dif < 0:
                    return False

                n_build = -dif
                k += dif

                cur_pow += n_build
                delta[min(n, i + 2 * r + 1)] -= n_build

            return True

        lo = min(stations)
        hi = max(stations) * (2 * r + 1) + k + 1

        ans = -1
        while lo < hi:
            m = lo + (hi - lo) // 2
            if possible(stations, r, k, m):
                ans = m
                lo = m + 1
            else:
                hi = m
        return ans
