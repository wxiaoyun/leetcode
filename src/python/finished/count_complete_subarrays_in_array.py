from typing import List

# https://leetcode.com/problems/count-complete-subarrays-in-an-array


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        s = set(nums)
        slen = len(s)

        r = 0
        cur = {}
        total = 0
        for l in range(N):
            while r < N and len(cur) < slen:
                rnum = nums[r]
                cur[rnum] = cur.get(rnum, 0) + 1
                r += 1

            if len(cur) == slen:
                total += N - r + 1

            lnum = nums[l]
            cur[lnum] = cur.get(lnum, 0) - 1
            if cur[lnum] == 0:
                del cur[lnum]

        return total
