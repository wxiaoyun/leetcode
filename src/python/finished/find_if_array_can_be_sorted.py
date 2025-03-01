from typing import List

# https://leetcode.com/problems/find-if-array-can-be-sorted

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def set_bits(a: int) -> int:
          cnt = 0
          cur = a
          while cur:
            rem = cur % 2
            if rem:
              cnt += 1
            cur = cur // 2
          return cnt

        prev_max = -float('inf')
        cur_max = -float('inf')
        cur_min = float('inf')
        prev_bit_cnt = -1

        for i, n in enumerate(nums):
          bit_cnt = set_bits(n)

          if bit_cnt == prev_bit_cnt:
            cur_max = max(cur_max, n)
            cur_min = min(cur_min, n)
            continue
          
          if prev_max > cur_min:
            return False
          
          prev_max = cur_max
          cur_max = n
          cur_min = n
          prev_bit_cnt = bit_cnt
          
        if prev_max > cur_min:
          return False
        return True

# class Solution:
#     def canSortArray(self, nums: List[int]) -> bool:
#         def set_bits(a: int) -> int:
#           cnt = 0
#           cur = a
#           while cur:
#             rem = cur % 2
#             if rem:
#               cnt += 1
#             cur = cur // 2
#           return cnt

#         prev_i = 0
#         prev_bit_cnt = -1

#         for i, n in enumerate(nums):
#           bit_cnt = set_bits(n)
#           print(n, bit_cnt)

#           if bit_cnt == prev_bit_cnt:
#             continue

#           nums[prev_i:i] = sorted(nums[prev_i:i])
#           prev_i = i
#           prev_bit_cnt = bit_cnt

#         nums[prev_i:] = sorted(nums[prev_i:])

#         for i in range(len(nums)-1):
#           if nums[i] > nums[i+1]:
#             return False
#         return True