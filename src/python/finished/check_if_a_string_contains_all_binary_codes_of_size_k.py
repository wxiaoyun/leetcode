# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        nums = [False] * (1 << k)

        mask = (1 << k) - 1
        cur = 0
        for i, ch in enumerate(s):
            bit = int(ch) & 1
            cur = (cur << 1 | bit) & mask

            if i >= k - 1:
                nums[cur] = True

        return all(nums)
