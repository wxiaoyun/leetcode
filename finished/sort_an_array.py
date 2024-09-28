# https://leetcode.com/problems/sort-an-array

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def partition(l: int, r: int) -> Tuple[int, int, int, int]:
#             pivot = nums[r]

#             i = l # pointer for the index for the next element smaller than pivot
#             for j in range(l, r):
#                 if nums[j] < pivot:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     i += 1

#             nums[i], nums[r] = nums[r], nums[i]
#             return i

#         def quicksort(l: int, r: int) -> None:
#             if (l >= r):
#                 return None

#             rp = random.randrange(l, r)
#             nums[r], nums[rp] = nums[rp], nums[r]

#             p = partition(l, r)
#             quicksort(l, p-1)
#             quicksort(p+1, r)

#         quicksort(0, len(nums) -1) 

#         return nums

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
      def merge(a: List[int], b: List[int]) -> List[int]:
        res = []

        i, j = 0, 0
        while i < len(a) and j < len(b):
          if a[i] < b[j]:
            res.append(a[i])
            i += 1
          else:
            res.append(b[j])
            j += 1

        res.extend(a[i:])
        res.extend(b[j:])
        return res

      def merge_sort(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
          return arr
        
        m = len(arr) // 2

        left = merge_sort(arr[:m])
        right = merge_sort(arr[m:])
        return merge(left, right)


      return merge_sort(nums)