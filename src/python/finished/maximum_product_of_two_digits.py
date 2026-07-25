import heapq

# https://leetcode.com/problems/maximum-product-of-two-digits


class Solution:
    def maxProduct(self, n: int) -> int:
        pq = []
        while n:
            heapq.heappush(pq, n % 10)
            if len(pq) > 2:
                heapq.heappop(pq)
            n //= 10

        ans = 1
        for num in pq:
            ans *= num
        return ans
