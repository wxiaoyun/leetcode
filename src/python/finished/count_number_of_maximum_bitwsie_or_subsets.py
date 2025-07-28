# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

# Time: O(n*max)
# Space: O(n*max)
from typing import Dict, List, Tuple


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for n in nums:
            mx |= n

        def helper(target: int, accum: int = 0, i: int = 0, dp: dict = {}) -> int:
            if i >= len(nums):
                return 1 if target == accum else 0

            key = (i, accum)
            if key in dp:
                return dp[key]

            cnt = helper(target, accum, i + 1)
            cnt += helper(target, accum | nums[i], i + 1)
            dp[key] = cnt
            return cnt

        return helper(mx)


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = 0
        for n in nums:
            maximum |= n

        dp: Dict[Tuple[int, int], int] = {}  # Dict[(idx, or_val), int]

        def helper(target: int, accum: int, i: int) -> int:
            key = (i, accum)
            if key in dp:
                return dp[key]

            res = 0
            # Continue to find other combinations
            if i >= len(nums):
                if accum == target:
                    res += 1
                return res

            # Take
            res += helper(maximum, accum | nums[i], i + 1)
            # No take
            res += helper(maximum, accum, i + 1)
            dp[key] = res
            return res

        return helper(maximum, 0, 0)


# Time: O(2^n)
# Space: O(1)
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = 0
        for n in nums:
            maximum |= n

        def helper(target: int, accum: int, i: int) -> int:
            res = 0
            # Continue to find other combinations
            if i >= len(nums):
                if accum == target:
                    res += 1
                return res

            # Take
            res += helper(maximum, accum | nums[i], i + 1)
            # No take
            res += helper(maximum, accum, i + 1)
            return res

        return helper(maximum, 0, 0)
