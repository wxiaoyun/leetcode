from typing import List

# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)
        lookup = [-1] * 31
        ret = [1] * N
        for i in reversed(range(N)):
            n = nums[i]
            r = i
            for b in range(31):
                if (n & (1 << b)) == 0:
                    if lookup[b] > 0:
                        r = max(r, lookup[b])
                else:
                    lookup[b] = i
            ret[i] = r - i + 1
        return ret


# O(N^2) TLE
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)

        ret = []
        for i in range(N):
            orr = nums[i]
            r = i
            for j in range(i + 1, N):
                test = orr | nums[j]
                if test > orr:
                    orr = test
                    r = j

            ret.append(r - i + 1)
        return ret
