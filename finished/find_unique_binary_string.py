from typing import List

# https://leetcode.com/problems/find-unique-binary-string

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])
        res = ["0"] * N

        for i, n in enumerate(nums):
            if n[i] == "1":
                continue
            res[i] = "1"
        return "".join(res)