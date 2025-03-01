from typing import List

# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # find start of the sorted array from the back:
        prev = float('inf')
        r = n-1
        while r >= 0 and arr[r] <= prev:
          prev = arr[r]
          r -= 1
        r += 1 # r was pointing at the index before the sorted array

        if r == 0:
          return 0 # array already sorted

        best = r
        prev = -float('inf')
        for l in range(n):
          if prev > arr[l]:
            break
          prev = arr[l]
          
          while r < n and arr[l] > arr[r]:
            r += 1
          
          if arr[l] <= (arr[r] if r < n else float('inf')):
            best = min(best, r-l-1)
        
        return best