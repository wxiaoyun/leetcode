from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + prices[i] * strategy[i])

        # maintain a window of length k
        # whenever we shift the window to the right:
        # 1. undo the strategy of on the right most pointer, then use the modified strategy
        # 2. undo the modified strategy of the middle element (so it becomes hold)
        # 3. redo the original strategy on the last element

        best = prefix_sum[-1]
        window = 0
        for i in range(n):
            # window:  ... L ... M ... R ...
            #              ^     ^     ^ i
            #                    i - k / 2
            #              i - k

            # sell
            window += prices[i]

            m = i - k // 2
            if m >= 0:
                # undo sell
                window -= prices[m]

            l = i - k
            # we have a window of k elements
            if i >= k - 1:
                left_of_window = prefix_sum[l + 1]
                right_of_window = prefix_sum[n] - prefix_sum[i + 1]

                best = max(best, left_of_window + window + right_of_window)

        return best
