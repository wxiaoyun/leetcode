from typing import List

# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)

        best, cur_max, diff_max = -1, nums[0], 0
        for k in range(1, N):
            cur = nums[k]
            best = max(best, diff_max * cur)
            diff_max = max(diff_max, cur_max - cur)
            cur_max = max(cur_max, cur)

        return best if best > 0 else 0

    def maximumTripletValue(self, nums: List[int]) -> int:
        posmax = [-float("inf")]

        N = len(nums)
        for i in range(N):
            j = N - i - 1
            posmax.append(max(posmax[-1], nums[j]))

        posmax.reverse()  # postfix max from N-1 to j, inclusive

        cur_max = nums[0]
        best = -float("inf")
        for i in range(1, N - 1):
            cur = nums[i]

            best = max(
                best,
                (cur_max - cur) * posmax[i + 1],
            )

            cur_max = max(cur_max, cur)

        return best if best > 0 else 0
