import heapq
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
  
  class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        pq = []

        for i, p in enumerate(prices):
            while pq:
                px, j = pq[0]
                px = -px

                if px < p:
                    break

                prices[j] -= p
                heapq.heappop(pq)
            
            heapq.heappush(pq, (-p, i))

        return prices