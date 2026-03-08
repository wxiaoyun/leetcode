from typing import List

# https://leetcode.com/problems/find-unique-binary-string


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = ["0"] * n

        for i in range(n):
            if nums[i][i] == "0":
                ans[i] = "1"
        return "".join(ans)


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])
        res = ["0"] * N

        for i, n in enumerate(nums):
            if n[i] == "1":
                continue
            res[i] = "1"
        return "".join(res)
