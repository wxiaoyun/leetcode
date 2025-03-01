from typing import Dict, List, Tuple

# https://leetcode.com/problems/target-sum/


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
