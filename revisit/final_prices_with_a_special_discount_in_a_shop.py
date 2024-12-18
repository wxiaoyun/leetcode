from typing import List

# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
      stack = []
      for i, p in enumerate(prices):
        while stack and prices[stack[-1]] >= p:
          j = stack.pop()
          prices[j] -= p
        stack.append(i)

      return prices