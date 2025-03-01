from typing import List

# https://leetcode.com/problems/count-the-number-of-fair-pairs/


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        arr = sorted(nums)
        N = len(arr)

        def search(l: int, r: int, target: int) -> int:
            while l < r:
                m = (l + r) // 2
                mid = arr[m]
                if mid < target:
                    l = m + 1
                else:
                    r = m
            return l

        # print(arr)
        pairs = 0
        for i in range(N - 1):
            cur = arr[i]

            lower_idx = search(i + 1, N, lower - cur)
            upper_idx = search(i + 1, N, upper - cur + 1)
            pairs += upper_idx - lower_idx

        return pairs


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()

        def lower_bound(low: int, high: int, target: int) -> int:
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low

        count = 0
        for j in range(1, n):
            lower_idx = lower_bound(0, j, lower - nums[j])
            upper_idx = lower_bound(0, j, upper - nums[j] + 1)
            count += upper_idx - lower_idx
        return count
