from typing import List

# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/


# O(n^2) TLE
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # let ways(i, j) = ways to partition nums[i..j]
        # let cond(i, j) = 1 if difference of max(nums[i..j]) and min(nums[i..j]) <= k else 0
        #
        # ways(i, i + 1) = 1
        # ways(i, j) = sum over k from i + 1 to j - 1:
        #    cond(i, k) * ways(k, j)

        dp = [-1] * len(nums)
        def compute(nums: List[int], i: int, limit: int) -> int:
            n = len(nums)
            if i == n:
                return 1

            if dp[i] >= 0:
                return dp[i]

            MOD = int(1e9) + 7

            ways = 0
            cur_min, cur_max = float('inf'), -float('inf')
            for k in range(i, n):
                knum = nums[k]
                cur_min = min(cur_min, knum)
                cur_max = max(cur_max, knum)

                if cur_max - cur_min > limit:
                    break

                ways = (ways + compute(nums, k + 1, limit)) % MOD

            dp[i] = ways
            return ways

        return compute(nums, 0, k)