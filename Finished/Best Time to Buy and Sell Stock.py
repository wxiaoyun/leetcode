# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# https://leetcode.com/problems/valid-palindrome/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Base case
        if (len(prices) <= 1):
            return 0

        # preprocess the maximum element reading from the right
        # max is monotonically non-increasing
        max = [0] * len(prices)
        max[-1] = prices[-1]

        for i in range(1, len(prices)):
            j = len(prices) - 1 - i
            if (prices[j] > max[j + 1]):
                max[j] = prices[j]
            else:
                max[j] = max[j + 1]

        # attempts to find the maximum profit
        maxProfit = 0
        for i in range(0, len(prices)):
            profit = max[i] - prices[i]
            if (profit < 0):
                continue # no profit
            elif (profit > maxProfit):
                maxProfit = profit
        return maxProfit