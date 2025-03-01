import heapq

# https://leetcode.com/problems/ugly-number-ii

class Solution:
    def nthUglyNumber(self, n: int) -> int:
      pq = [1]
      seen = set([1])
      for i in range(n-1):
        ugly = heapq.heappop(pq)
        # print(ugly)
        for u in [2, 3, 5]:
          new_ugly = ugly * u
          if new_ugly not in seen:
            heapq.heappush(pq, ugly * u)
            seen.add(new_ugly)
      return heapq.heappop(pq)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
      # # Heap
      # # Time O(nlogn)
      # # Space O(n)
      # # each iteration we add at most 3 numbers, for n iterations. So heap size is O(n)
      # pq = [1]

      # seen = set([1])
      
      # cur = 1
      # for _ in range(n):
      #   cur = heapq.heappop(pq)

      #   for fact in [2, 3, 5]:
      #     next = cur * fact
      #     if next not in seen:
      #       heapq.heappush(pq, next)
      #       seen.add(next)
      
      # return cur

      # dp
      # Time O(n)
      # Space O(n)
      dp = [1] * n
      idx_2, idx_3, idx_5 = 0, 0, 0
      next_2, next_3, next_5 = 2, 3, 5

      for i in range(1, n):
        _next = min(next_2, next_3, next_5)
        dp[i] = _next
        
        if _next == next_2:
          idx_2 += 1
          next_2 = dp[idx_2] * 2
        if _next == next_3:
          idx_3 += 1
          next_3 = dp[idx_3] * 3
        if _next == next_5:
          idx_5 += 1
          next_5 = dp[idx_5] * 5
      
      return dp[-1]