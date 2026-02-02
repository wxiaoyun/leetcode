from typing import List

from sortedcontainers import SortedList

# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # I wish to have a sliding window of size dist, such that
        # I know the minimum k elements within the window

        kk = k - 1
        sl = SortedList()
        win_sum = 0
        best = 1 << 63
        for i in range(1, len(nums)):
            n = nums[i]
            sl.add((n, i))

            idx = sl.index((n, i))
            if idx < kk:
                win_sum += n

                if len(sl) > kk:
                    win_sum -= sl[kk][0]

            # i_{k-1} - i_1 <= dist
            # i_1 >= i_{k-1} - dist
            # i_ 1 > i_{k-1} - dist - 1
            if i - dist - 1 >= 1:
                j = i - dist - 1
                n = nums[j]
                if (n, j) in sl:
                    idx = sl.index((n, j))
                    sl.pop(idx)

                    if idx < kk:
                        win_sum -= n

                        if len(sl) >= kk:
                            win_sum += sl[kk - 1][0]

            if len(sl) >= kk:
                best = min(best, win_sum)

        return best + nums[0]
