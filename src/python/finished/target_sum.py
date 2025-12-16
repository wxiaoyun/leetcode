from typing import Dict, List, Tuple

# https://leetcode.com/problems/target-sum/


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def compute(dp: dict, nums: int, i: int, target: int) -> int:
            if i >= len(nums):
                if target == 0:
                    return 1
                return 0

            key = (i, target)
            if key in dp:
                return dp[key]

            ways = 0
            for n in [nums[i], -nums[i]]:
                ways += compute(dp, nums, i + 1, target - n)
            dp[key] = ways
            return ways

        return compute({}, nums, 0, target)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp: Dict[Tuple[int, int], int] = {}

        def find(cur: int, idx: int) -> int:
            if idx >= len(nums):
                if cur == 0:
                    return 1
                else:
                    return 0

            key = (cur, idx)
            if key in dp:
                return dp[key]

            n = nums[idx]

            # add
            count = find(cur - n, idx + 1)

            # subtract
            count += find(cur + n, idx + 1)

            dp[key] = count
            return count

        return find(target, 0)
