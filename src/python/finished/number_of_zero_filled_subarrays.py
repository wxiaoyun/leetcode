# https://leetcode.com/problems/number-of-zero-filled-subarrays/


from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeros = []
        cur, count = -1, 0
        for n in nums:
            if n == cur:
                count += 1
                continue

            if cur == 0:
                zeros.append(count)

            cur = n
            count = 1

        if cur == 0:
            zeros.append(count)

        return sum(z * (z + 1) // 2 for z in zeros)
