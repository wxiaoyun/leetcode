from typing import List

# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # observation:
        # - x OR x + 1 is always odd
        #  111 OR 1000 = 1111
        #  110 OR 111 = 111
        #  x OR x + 1 sets the least significant 0 bit to 1

        ans = [-1] * len(nums)
        for i, n in enumerate(nums):
            if n % 2 == 0:
                continue

            # find the most significant 1 bit BEFORE any 0 bit:
            # 11011011111
            #       ^

            bit = 0
            cur = n
            while cur > 0:
                if cur & 1 == 0:
                    break

                bit += 1
                cur >>= 1
            ans[i] = n - (1 << (bit - 1))

        return ans
