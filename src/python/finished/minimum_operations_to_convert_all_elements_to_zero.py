from typing import List

# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/


# Monotonic Stack O(n)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        cuts = [0]  # monotonically non-decreasing
        for n in nums:
            while n < cuts[-1]:
                cuts.pop()

            if n > cuts[-1]:
                cuts.append(n)
                ops += 1

        return ops


# Binary Search O(nlogn)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def possible(arr: list, ops: int) -> bool:
            remaining_ops = ops

            cuts = [0]  # monotonically non-decreasing
            for n in arr:
                while n < cuts[-1]:
                    cuts.pop()

                additional_ops = 0
                if n > cuts[-1]:
                    cuts.append(n)
                    additional_ops = 1

                if additional_ops > remaining_ops:
                    return False
                remaining_ops -= additional_ops

            return True

        lo, hi = 0, sum(nums) + 1
        ans = -1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if possible(nums, mi):
                ans = mi
                hi = mi
            else:
                lo = mi + 1
        return ans


# TLE: O(n^2)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def helper(arr: list, l: int, r: int) -> int:
            if l >= r:
                return 0

            minn = min(arr[l:r])
            steps = 0 if minn == 0 else 1
            prev = l
            for i in range(l, r):
                if arr[i] != minn:
                    continue

                steps += helper(arr, prev, i)
                prev = i + 1

            steps += helper(arr, prev, r)
            return steps

        return helper(nums, 0, len(nums))
