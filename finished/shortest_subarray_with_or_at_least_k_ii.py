from typing import List

# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_len = float('inf')
        bin_count = [0] * 32 # LSB to MSB
        cur_num = 0 # OR[i, i+1, ..., j-1]
        j = 0
        for i in range(n):
          while j-i == 0 or cur_num < k:
            if j >= n:
              break

            j_num = nums[j]
            cur_num |= j_num

            j_num_bin = bin(j_num)[2:]
            for kk, c in enumerate(reversed(j_num_bin)):
              if c == '1':
                bin_count[kk] += 1
            j += 1
          
          if cur_num >= k:
            min_len = min(min_len, j-i)

          i_num = nums[i]
          i_num_bin = bin(i_num)[2:]
          for kk, c in enumerate(reversed(i_num_bin)):
            if c == '1':
              bin_count[kk] -= 1
          
          tmp = reversed(["1" if cnt > 0 else "0" for cnt in bin_count])
          cur_num = int("".join(tmp), 2)
        
        return min_len if min_len < float('inf') else -1
