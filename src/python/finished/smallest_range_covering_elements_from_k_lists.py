import heapq
from typing import List, Tuple

# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

# Time: O(nlogn)
# Space: O(n)
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        N = len(nums)

        combined = []
        for i, arr in enumerate(nums):
          combined.extend([(n, i) for n in arr])
        combined.sort()

        freq, count = [0] * N, 0
        lo, hi = -float('inf'), float('inf')
        left = 0 

        for right, (n, i) in enumerate(combined):
          freq[i] += 1
          if freq[i] == 1:
            count += 1
          
          while count == N:
            n_left, idx_left = combined[left]
            if n - n_left < hi - lo:
              hi = n
              lo = n_left

            freq[idx_left] -= 1
            if freq[idx_left] == 0:
              count -= 1
            left += 1
        
        return [lo, hi]

# Heap improved
# Time: O(nlogk)
# Space: O(k)
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        N = len(nums)
        
        cur_hi = -1
        lo, hi = -float('inf'), float('inf')
        pq: List[Tuple[int, int, int]] = [] # [][num, row, col]
        for i in range(N):
          heapq.heappush(pq, (nums[i][0], i, 0))
          cur_hi = max(cur_hi, nums[i][0])
        
        while len(pq) == N:
          cur_lo, r, c = heapq.heappop(pq)
          if cur_hi - cur_lo < hi - lo:
            hi, lo = cur_hi, cur_lo

          if c+1 < len(nums[r]): # Find a replacement if possible
            heapq.heappush(pq, (nums[r][c+1], r, c+1))
            cur_hi = max(cur_hi, nums[r][c+1])

        return [lo, hi]
      
# Time: O(nklogn)
# Space: O(n+k)
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        N = len(nums)

        cur_nums = [(arr[0], i) for i, arr in enumerate(nums)]
        lo = min(cur_nums)
        hi = max(cur_nums)
        best = [lo[0], hi[0]]
        best_dist = hi[0] - lo[0]

        all_nums: List[Tuple[int, int]] = []
        for i, arr in enumerate(nums):
          all_nums.extend([(n, i) for n in arr[1:]])
        heapq.heapify(all_nums)

        while all_nums:
          while all_nums:
            item = heapq.heappop(all_nums)
            cur_nums[item[1]] = item
            if item[1] == lo[1]:
              break
          
          lo = min(cur_nums)
          hi = max(cur_nums)
          if hi[0] - lo[0] < best_dist:
            best = [lo[0], hi[0]]
            best_dist = hi[0] - lo[0]

        return best