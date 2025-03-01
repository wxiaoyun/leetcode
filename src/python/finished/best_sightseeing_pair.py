import heapq
from typing import List

# https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    # O(n) time, O(1) space
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
      N = len(values)

      max_left_score = values[0]
      best = -1

      for j in range(1, N):
        best = max(best, max_left_score + values[j] - j)
        max_left_score = max(max_left_score, values[j] + j)
      
      return best

    # O(nlogn) time, O(n) space
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)

        pq = [] # MaxHeap<(score, value, i)>
        best = -1
        for j, v in enumerate(values):
          if pq:
            _, vv, i = pq[0]
            best = max(best, v + vv + i - j)
          
          score = - v - j
          heapq.heappush(pq, (score, v, j))

        return best


    # O(n^2) time, O(1) space
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        N = len(values)

        best = -1
        for i in range(N):
          for j in range(i+1, N):
            best = max(best, values[i] + values[j] + i - j)
        return best