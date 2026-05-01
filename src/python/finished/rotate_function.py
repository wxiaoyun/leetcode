from typing import List

# https://leetcode.com/problems/rotate-function


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(0) =       0 * arr[0] + ... + (n - 1)         * arr[n - 1]
        # F(1) = (0 + 1) * arr[0] + ... + (n - 1 + 1) % n * arr[n - 1]
        # F(2) = (0 + 2) * arr[0] + ... + (n - 1 + 2)

        # F(j) = Sum i {(i + j) % n * arr[i]}

        # can we be greedy? Rotate k such that largest number is the last. Idts..

        # F(j) = F(j - 1) + sum(arr) - arr[(n - j) % n] * (n - 1)

        n = len(nums)
        total = 0
        dp = 0
        for i in range(n):
            dp += i * nums[i]
            total += nums[i]

        best = dp
        for j in range(1, n):
            dp = dp + total - nums[(n - j) % n] * n
            best = max(best, dp)
        # print(list(enumerate(dp)))
        return best
