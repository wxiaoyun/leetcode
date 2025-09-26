from typing import List

# https://leetcode.com/problems/valid-triangle-number/


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        triplets = 0
        for i in range(n - 2):
            if nums[i] == 0:
                continue

            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                triplets += k - j - 1

        return triplets


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def search(arr: List[int], target: int, left: int, right: int) -> int:
            # find greatest element that is smaller than target
            l, r = left, right
            ans = -1

            while l < r:
                m = l + (r - l) // 2
                mid = arr[m]

                if mid < target:
                    ans = m
                    l = m + 1
                else:
                    r = m

            return ans

        nums.sort()
        triplets = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                bound = search(nums, nums[i] + nums[j], j + 1, len(nums))
                if bound < 0:
                    continue

                triplets += bound - j

        return triplets
