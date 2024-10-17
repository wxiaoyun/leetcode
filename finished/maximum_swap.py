# https://leetcode.com/problems/maximum-swap/

from typing import List, Tuple

# Solution 2: Prefix min
# Time: O(n)
class Solution:
    def maximumSwap(self, num: int) -> int:
      num = [c for c in str(num)]
      N = len(num)

      prefix_min: List[Tuple[int, int]] = [None] * N # List[[digit, index]]
      suffix_max: List[Tuple[int, int]] = [None] * N # List[[digit, index]]

      for i in range(N):
        j = N-i-1

        if i == 0:
          prefix_min[i] = (num[i], i)
          suffix_max[j] = (num[j], j)
          continue
        
        if prefix_min[i-1][0] <= num[i]:
          prefix_min[i] = prefix_min[i-1]
        else:
          prefix_min[i] = (num[i], i)

        if suffix_max[j+1][0] >= num[j]:
          suffix_max[j] = suffix_max[j+1]
        else:
          suffix_max[j] = (num[j], j)
      
      for i in range(N):
        pmd, pmi = prefix_min[i]
        smd, smi = suffix_max[i]

        if pmd < smd:
          num[pmi], num[smi] = num[smi], num[pmi]
          break
      
      return int("".join(num))

# Solution 1: Selection Sort
# Time: O(n^2)
# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         num = [c for c in str(num)]

#         for i in range(len(num)):
#           max_i = i

#           for j in range(i+1, len(num)):
#             if num[j] >= num[max_i]:
#               max_i = j
  
#           if num[max_i] != num[i]:
#             num[max_i] , num[i] = num[i], num[max_i]
#             break
          
#         return int("".join(num))