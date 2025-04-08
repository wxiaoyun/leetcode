from typing import List

# https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        threes = N // 3
        rem = N % 3

        seen = set()
        j = N - 1
        for _ in range(rem):
            n = nums[j]
            if n in seen:
                return threes + 1

            seen.add(n)
            j -= 1

        for cnt in range(threes):
            for _ in range(3):
                n = nums[j]
                if n in seen:
                    return threes - cnt

                seen.add(n)
                j -= 1

        return 0
