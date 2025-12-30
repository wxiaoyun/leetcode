from typing import List

# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        best = -(1 << 31)
        one_del = best
        zero_del = best

        for n in arr:
            # delete 1 element from the zero_del streak or continue the current streak
            one_del = max(zero_del, one_del + n)
            zero_del = max(n, zero_del + n)
            best = max(best, one_del, zero_del)
        return best


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        res = -float("inf")
        # maximum subarray with no deletion
        best = -float("inf")
        # maximum subarray with 1 deletion
        best_del = -float("inf")
        for n in arr:
            # either a continue a streak with 1 deleted element
            # or start a new streak with n deleted
            best_del = max(best_del + n, best)
            best = max(best + n, n)
            res = max(res, best, best_del)
        return res
