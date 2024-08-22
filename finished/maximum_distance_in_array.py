# https://leetcode.com/problems/maximum-distance-in-arrays/

import heapq
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Brute force
        # Time O(n^2) 
        # Space O(1)
        # N = len(arrays)
        # _max = -1

        # for i in range(N):
        #   for j in range(i+1, N):
        #     _max = max(
        #       _max,
        #       abs(arrays[i][0] - arrays[j][-1]),
        #       abs(arrays[i][-1] - arrays[j][0])
        #     )
        
        # return _max

        # Sorting
        # Time O(nlogn)
        # Space O(n)
        # mins = sorted([(elm[0], idx) for (idx, elm) in enumerate(arrays)])
        # maxs = sorted([(elm[-1], idx) for (idx, elm) in enumerate(arrays)])

        # return maxs[-1][0] - mins[0][0] if mins[0][1] != maxs[-1][1] else max(
        #   maxs[-1][0] - mins[1][0],
        #   maxs[-2][0] - mins[0][0]
        # )

        # Fixed sized heap
        # Time O(n)
        # Space O(1)
        mins = []
        maxs = []

        for (idx, arr) in enumerate(arrays):
          _min = (-arr[0], idx) # max heap to remove larger elements
          _max = (arr[-1], idx) # min heap to remove small elements

          heapq.heappush(mins, _min)
          heapq.heappush(maxs, _max)

          while len(mins) > 2:
            heapq.heappop(mins)
          while len(maxs) > 2:
            heapq.heappop(maxs)
  
        return maxs[-1][0] + mins[-1][0] if mins[-1][1] != maxs[-1][1] else max(
          maxs[-1][0] + mins[0][0],
          maxs[0][0] + mins[-1][0]
        )
        