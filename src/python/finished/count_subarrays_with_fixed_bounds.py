from typing import List

# https://leetcode.com/problems/count-subarrays-with-fixed-bounds


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def count_continguous(arr: List[int], k: int) -> List[int]:
            N = len(arr)
            res = []
            i = 0
            while i < N:
                while i < N and arr[i] != k:
                    i += 1

                count = 0
                while i < N and arr[i] == k:
                    count += 1
                    i += 1

                if count > 0:
                    res.append(count)
            return res

        if minK == maxK:
            segs = count_continguous(nums, minK)
            return sum([s * (s + 1) // 2 for s in segs])  # (s + 1) choose 2

        def split_subarray(arr: List[int], mn: int, mx: int) -> List[List[int]]:
            N = len(arr)
            res = []
            i = 0

            while i < N:
                while i < N and (arr[i] < mn or arr[i] > mx):
                    i += 1

                subarr = []
                while i < N and (arr[i] >= mn and arr[i] <= mx):
                    subarr.append(arr[i])
                    i += 1

                if len(subarr) > 0:
                    res.append(subarr)

            return res

        subarrays = split_subarray(nums, minK, maxK)
        # print(subarrays)

        def count(arr: List[int], mn: int, mx: int) -> int:
            N = len(arr)
            mn_i, mx_i = -1, -1
            # print(arr)

            count = 0
            for i, n in enumerate(arr):
                if n == mn:
                    mn_i = i
                elif n == mx:
                    mx_i = i

                count += min(mn_i, mx_i) + 1
                # print(mn_i, mx_i, min(mn_i, mx_i), i)

            return count

        return sum([count(arr, minK, maxK) for arr in subarrays])
